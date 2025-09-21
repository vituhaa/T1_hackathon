from openai import OpenAI
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import json
import re

import sys
from pathlib import Path
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DataBase.dbconnect import get_all_as_json
from DataBase.skills_required import get_skills_required_for_position
from DataBase.skills_to_employees import get_all_skills_employee
from set_chroma import reset_collection, add_item_to_chroma, query_chroma, semantic_search, get_chat_history, add_chat_message

# ====== КЛИЕНТ OpenAI ======
client = OpenAI(api_key="sk-qAVtgeSNioNomveOtt17ZQ", base_url="https://llm.t1v.scibox.tech/v1")

# ====== ЗАГРУЗКА ДАННЫХ ======

# positions =json.loads(get_all_as_json('Positions'))
# courses = json.loads(get_all_as_json('Learning_courses'))
employees = json.loads(get_all_as_json('Employees'))
skills_to_employees = json.loads(get_all_as_json('skills_to_employees'))
skills = json.loads(get_all_as_json('Skills'))


skills_map = {s['id']: s['name'] for s in skills}
name_to_skill_id = {name: skill_id for skill_id, name in skills_map.items()}


# ====== СИСТЕМА ======

# def prepare_item_text(item):
#         if "link" in item:  # курс
#             skill_id = item['skill_id']
#             skill = skills_map[skill_id] if skill_id in skills_map else "No skill"
#             return f"{item['title']} {item['link']} {skill}"
#         else:  # position
#             skill_ids = get_skills_required_for_position(item['id'])
#             skills = [skills_map[skill_id] for skill_id in skill_ids if skill_id in skills_map]
#             return f"{item['name']} {item['description']} {item['created_at']} {item['is_closed']} {' '.join(skills)}"
        

class CareerRAGSystem:
    def __init__(self):
        print("Это просто заглушка")
    #     reset_collection()
    #     self._load_to_chroma()

    # def _load_to_chroma(self):
    #     for c in courses:
    #         text = prepare_item_text(c)
    #         skill_id = c['skill_id']
    #         skill = skills_map[skill_id] if skill_id in skills_map else "No skill"
    #         metadata = {
    #             "type": "course",
    #             "course_id": c["id"],
    #             "title": c["title"],
    #             "link": c["link"],
    #             "skill": skill
    #         }
    #         add_item_to_chroma(f"course_{c['id']}", text, metadata)

    #     for p in positions:
    #         text = prepare_item_text(p)
    #         skill_ids = get_skills_required_for_position(p['id'])
    #         skills = [skills_map[skill_id] for skill_id in skill_ids if skill_id in skills_map]

    #         metadata = {
    #             "type": "position",
    #             "position_id": p["id"],
    #             "name": p["name"],
    #             "description": p.get("description"),
    #             "created_at": str(p.get("created_at")),
    #             "is_closed": p.get("is_closed"),
    #             "skills": ",".join(skills)
    #         }
    #         add_item_to_chroma(f"position_{p['id']}", text, metadata)

    def get_recommendations(self, user_skills, top_k=3):
        query_text = f"Навыки сотрудника: {', '.join(user_skills)}. Какие курсы и вакансии подходят?"
        results = query_chroma(query_text, n=top_k*2)

        courses_out, positions_out = [], []
        for r in results:
            meta = r["metadata"]
            if meta["type"] == "course":
                courses_out.append({
                    "id": meta["id"],
                    "title": meta["title"],
                    "link": meta["link"],
                    "match_score": round(float(r["score"]), 3)
                })
            elif meta["type"] == "position":
                positions_out.append({
                    "id": meta["id"],
                    "name": meta["name"],
                    "description": meta["description"][:120] + "...",
                    "match_score": round(float(r["score"]), 3)
                })

        return {"courses": courses_out[:top_k], "positions": positions_out[:top_k]}
        
    # def find_similar_items(self, query, top_k=5):
    #     query_embedding = self.get_embedding(query)
    #     similarities = cosine_similarity([query_embedding], self.embeddings)
    #     most_similar_indices = np.argsort(similarities[0])[-top_k:][::-1]

    #     results = []
    #     for idx in most_similar_indices:
    #         item = self.knowledge_base[idx]
    #         results.append({
    #             'item': item,
    #             'score': similarities[0][idx]
    #         })
    #     return results



    # def get_recommendations(self, user_skills, top_k=3):
    #     query_text = f"Навыки сотрудника: {', '.join(user_skills)}. Поиск курсов и вакансий для развития карьеры."

    #     similar_items = self.find_similar_items(query_text, top_k=top_k*2)

    #     courses = []
    #     positions = []

    #     for item_data in similar_items:
    #         item = item_data['item']
    #         score = item_data['score']
    #         if score < 0.2:
    #             continue

    #         if item['type'] == 'learning_courses':
    #             courses.append({
    #                 "id": item["id"],
    #                 "title": item["title"],
    #                 "match_score": round(float(score), 3),
    #                 "link": item["link"]
    #             })
    #         elif item['type'] == 'positions':
    #             positions.append({
    #                 "id": item["id"],
    #                 "name": item["name"],
    #                 "description": item["description"][:120] + "..." if len(item["description"]) > 120 else item["description"],
    #                 "match_score": round(float(score), 3),
    #                 "created at": item["created_at"],
    #                 "is closed": item['is_closed']
    #             })

    #     return {
    #         "courses": courses[:top_k],
    #         "positions": positions[:top_k]
    #     }
    
    
    

    def build_career_dialogue(self,employee_id, user_message, target_position_id=None):
        # Получаем сотрудника
        employee = next((emp for emp in employees if emp['id'] == employee_id), None)
        if not employee:
            return {"error": "Сотрудник не найден"}

        # Навыки сотрудника
        skill_emp_ids = [row['skill_id'] for row in get_all_skills_employee(employee_id)]
        skills_emp = [skills_map[skill_id] for skill_id in skill_emp_ids if skill_id in skills_map]

        # -----------------------------
        # 1. Выбор позиции через Chroma
        # -----------------------------
        if not target_position_id:
            positions_query = f"Навыки сотрудника: {skills_emp}. Сообщение: {user_message}"
            chroma_results = query_chroma(positions_query, n=5)

            # Фильтруем только позиции
            positions_matches = [r for r in chroma_results if r['metadata'].get('type') == 'position']
            if not positions_matches:
                return {"error": "Не удалось найти подходящую позицию"}
            

            best_match = positions_matches[0]
            target_position_id = best_match['metadata']['position_id']

        # Получаем данные выбранной позиции
        target_position = best_match['metadata']

        # Навыки позиции
        position_skills = target_position.get('skills').split(",")
        

        # -----------------------------
        # 2. Подбор курсов через Chroma
        # -----------------------------
        courses_for_skills = []
        for skill in position_skills:
            # Ищем курсы с таким skill_id
            course_results = query_chroma(f"skill:{skill}", n=5)
            courses = [r for r in course_results if r['metadata'].get('type') == 'course']
            courses_for_skills.extend(courses)

        # Убираем дубликаты курсов по course_id
        # seen_course_ids = set()
        # unique_courses = []
        # for c in courses_for_skills:
        #     if c not in seen_course_ids:
        #         unique_courses.append(c)
        #         seen_course_ids.add(c)

        print(courses_for_skills)

        # -----------------------------
        # 3. Формируем текст для LLM
        # -----------------------------
        pos_text = f"Целевая позиция: {target_position.get('name','')}.\n" \
                f"Описание: {target_position.get('description','')}.\n" \
                f"Требуемые навыки: {', '.join(position_skills)}\n" \
                f"Рекомендованные курсы: {', '.join([c['metadata']['title'] for c in courses_for_skills])}"

        prompt = f"""
        Сотрудник: {employee['first_name']} {employee['last_name']}
        Его навыки: {skills_emp}
        {pos_text}

        Сообщение сотрудника: "{user_message}"

        Твоя задача:
        - Общайся в живом диалоге, а не сухими фактами.
        - Сначала оцени текущие навыки и желание сотрудника.
        - Укажи недостающие компетенции.
        - Подбери курсы из базы знаний (courses), которые помогут.
        - Составь пошаговый карьерный план.
        - Верни ответ в естественной речи (чтобы выглядело как диалог).
        """

        response = client.chat.completions.create(
            model="Qwen2.5-72B-Instruct-AWQ",
            messages=[
                {"role": "system", "content": "Ты карьерный консультант HR, отвечай дружелюбно и полезно."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content
    
    def chat(self,employee_id, user_message, other_materials=None):
        add_chat_message(employee_id, "user", user_message)

        history = get_chat_history(employee_id, limit=10)

        knowledge = semantic_search(user_message,top_k=2)

        context = "\n\n".join([
            f"[{h['role']}] {h['content']}" for h in history
        ])
        knowledge_text = "\n\n".join([
            f"[{k['type']}] {k['content']}" for k in knowledge
        ])


        prompt = f"""
            Ты HR-ассистент компании.
            История диалога:
            {context}

            Релевантные материалы, ищи только тут, предлагать другие курсы нельзя:
            {knowledge_text}
            {other_materials if other_materials else " "}

            Вопрос сотрудника:
            {user_message}

            Дай понятный и дружелюбный ответ.
        """

        response = client.chat.completions.create(
            model="Qwen2.5-72B-Instruct-AWQ",
            messages=[{"role": "system", "content": "Ты помощник HR отдела."},
                    {"role": "user", "content": prompt}]
        )
        reply = response.choices[0].message.content
        add_chat_message(employee_id, "assistant", reply)
        return reply



# ====== API-ФУНКЦИЯ ======
def get_recommendations_for_employee(employee_id: str, rag_system: CareerRAGSystem):
    """
    Получение рекомендаций для сотрудника по ID.
    Профиль читаем из employees.json, рекомендации считаем в реальном времени.
    """
    employee = next((emp for emp in employees if emp['id'] == employee_id), None)
    if not employee:
        return {"error": "Сотрудник не найден"}
    
    skill_emp_ids = [row['skill_id'] for row in get_all_skills_employee(employee_id)]
    skills_emp = [skills_map[skill_id] for skill_id in skill_emp_ids if skill_id in skills_map]

    recommendations = rag_system.get_recommendations(skills_emp)

    return {
        "employee": {
            "id": employee['id'],
            "name": employee['first_name'],
            "last name": employee['last_name']
        },
        "recommendations": recommendations
    }

def get_career_plan_for_employee(employee_id, rag_system,user_message,target_position_id=None):
    employee = next((emp for emp in employees if emp['id'] == employee_id), None)
    if not employee:
        return {"error": "Сотрудник не найден"}
    
    skill_emp_ids = [row['skill_id'] for row in get_all_skills_employee(employee_id)]
    skills_emp = [skills_map[skill_id] for skill_id in skill_emp_ids if skill_id in skills_map]

    if not target_position_id:
            positions_query = f"Навыки сотрудника: {skills_emp}. Сообщение: {user_message}"
            chroma_results = semantic_search(positions_query)

            # Фильтруем только позиции
            positions_matches = [r for r in chroma_results if r.get('type') == 'position']
            if not positions_matches:
                return {"error": "Не удалось найти подходящую позицию"}
            

            best_match = positions_matches[0]
            target_position_id = best_match['metadata']['position_id']

        # Получаем данные выбранной позиции
    target_position = best_match['metadata']

    # Навыки позиции
    position_skills = target_position.get('skills').split(",")
    

    # -----------------------------
    # 2. Подбор курсов через Chroma
    # -----------------------------
    courses_for_skills = []
    for skill in position_skills:
        # Ищем курсы с таким skill_id
        course_results = semantic_search(f"skill:{skill}")
        courses = [r for r in course_results if r.get('type') == 'course']
        courses_for_skills.extend(courses)

    # Убираем дубликаты курсов по course_id
    # seen_course_ids = set()
    # unique_courses = []
    # for c in courses_for_skills:
    #     if c not in seen_course_ids:
    #         unique_courses.append(c)
    #         seen_course_ids.add(c)


    # -----------------------------
    # 3. Формируем текст для LLM
    # -----------------------------
    pos_text = f"Целевая позиция: {target_position.get('name','')}.\n" \
            f"Описание: {target_position.get('description','')}.\n" \
            f"Требуемые навыки: {', '.join(position_skills)}\n" \
            f"Рекомендованные курсы: {', '.join([c['title'] for c in courses_for_skills])}"
    
    return rag_system.chat(employee_id,user_message,pos_text)

# ====== ПРИМЕР ЗАПУСКА ======

# один раз инициализируем систему
rag_system = CareerRAGSystem()

# пример запроса к API
reply = get_career_plan_for_employee(1,rag_system,"Привет! Я хочу стать ML инженером, как мне это сделать?")
