from DataBase.employees import *
from DataBase.skills import *
from DataBase.skills_to_employees import *
from DataBase.projects import *

import chromadb

from typing import List, Dict
import numpy as np
from openai import OpenAI

class EmployeeVectorSearch:
    def __init__(self):
        self.openAI = OpenAI(api_key="sk-qAVtgeSNioNomveOtt17ZQ", base_url="https://llm.t1v.scibox.tech/v1")
        # Инициализируем Chroma DB
        self.client = chromadb.CloudClient(
  api_key='ck-4ZFsyeB8oj5ENE2XW9djHrCuvPvLD5kq3Ljrk32J5bFh',
  tenant='16c8626a-7b9d-41ed-a0df-2c64504e4689',
  database='t1_'
)
        self.collection = self.client.get_or_create_collection(
            name="employees",
            metadata={"description": "База сотрудников для семантического поиска"}
        )
    
    def get_embedding(self, text):
        emb = self.openAI.embeddings.create(
            model="bge-m3",
            input=[text],
        )
        return emb.data[0].embedding
    
    def get_employee_profile_text(self, employee_id: int) -> str:

        profile_parts = []
    
    # 2. Навыки с уровнями
        skills = get_all_skills_employee(employee_id)
        skill_details = []
        for skill_data in skills:
        # Нужно получить название навыка по skill_id
            skill_name = get_skill(skill_data['skill_id'])['name']
            if skill_name:
                skill_details.append(f"{skill_name} {skill_data['skill_level']}")
    
        if skill_details:
            profile_parts.append("Навыки: " + ", ".join(skill_details))
    
    # 3. Проекты и роли
        projects = get_all_projects(employee_id)
        project_details = []
        for project in projects:
            project_str = f"{project['project_name']}, {project['role']}"
            project_details.append(project_str)
    
        if project_details:
            profile_parts.append("Проекты: " + "; ".join(project_details))
    
    # 4. Здесь можно добавить другие данные (образование, опыт и т.д.)
    # из таблицы profile_completeness и data.json
    
        return " ".join(profile_parts)
    
    def add_employee_to_vector_db(self, employee_id: int):
        """
        Добавляем сотрудника в векторную БД
        """
        profile_text = self.get_employee_profile_text(employee_id)
        embedding = self.get_embedding(profile_text)

        self.collection.add(
            ids=[str(employee_id)],
            embeddings=[embedding],
            documents=[profile_text],
            metadatas=[{"employee_id": employee_id}]
        )
        
        print(f"Сотрудник {employee_id} добавлен в векторную БД")
    
    def search_similar_employees(self, query: str, limit: int = 5) -> List[Dict]:

        # Векторизуем запрос
        query_embedding = self.get_embedding(query)
        
        # Ищем в векторной БД
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=limit,
            include=['distances', 'documents', 'metadatas']
        )
        
        # Форматируем результаты
        similar_employees = []
        for i in range(len(results['ids'][0])):
            employee_id = int(results['ids'][0][i])
            distance = results['distances'][0][i]
            score = 1 - distance  # преобразуем расстояние в score (0-1)
            document = results['documents'][0][i]
            
            # Получаем полную информацию о сотруднике
            employee = get_employee(employee_id)
            skills = get_all_skills_employee(employee_id)
            
            similar_employees.append({
                'id': employee_id,
                'name': f"{employee['first_name']} {employee['last_name']}",
                'email': employee['email'],
                'match_score': round(score, 3),
                'skills': [f"{get_skill(s['skill_id'])['name']} {s['skill_level']}" for s in skills],
                'profile_snippet': document[:200] + "..." if len(document) > 200 else document
            })
        
        return similar_employees
    
    def initialize_database(self):
        """
        Инициализация БД для всех сотрудников
        """
        # Получаем всех сотрудников
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM Employees")
        employee_ids = [row[0] for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        
        # Добавляем каждого сотрудника в векторную БД
        for employee_id in employee_ids:
            try:
                self.add_employee_to_vector_db(employee_id)
            except Exception as e:
                print(f"Ошибка при обработке сотрудника {employee_id}: {e}")

# Использование
if __name__ == "__main__":
    # Инициализируем систему
    search_system = EmployeeVectorSearch()
    
    # Заполняем базу данными всех сотрудников
    # search_system.initialize_database()
    
    # Пример поиска
    query = "Эксперт Python"
    results = search_system.search_similar_employees(query, limit=5)
    
    print(f"Результаты поиска для: '{query}'")
    print("=" * 50)
    
    for i, result in enumerate(results, 1):
        print(f"{i}. {result['id']} (Score: {result['match_score']})")
        print(f"   Навыки: {', '.join(result['skills'][:3])}...")
        print(f"   {result['profile_snippet']}")
        print()

