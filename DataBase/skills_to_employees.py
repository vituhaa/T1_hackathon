import sys
from pathlib import Path

project_root = Path(__file__).parent
sys.path.append(str(project_root))

from dbconnect import get_connection

"""CREATE TABLE skills_to_employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT NOT NULL,
    skill_id INT NOT NULL,
    skill_level ENUM('beginner', 'intermediate', 'advanced', 'expert') NOT NULL,

    CONSTRAINT fk_ste_employee FOREIGN KEY (employee_id)
        REFERENCES Employees(id) ON DELETE CASCADE,

    CONSTRAINT fk_ste_skill FOREIGN KEY (skill_id)
        REFERENCES Skills(id) ON DELETE CASCADE,

    UNIQUE KEY uq_employee_skill (employee_id, skill_id)
);
"""

def add_skill_to_employee(employee_id, skill_id, skill_level):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO skills_to_employees (employee_id, skill_id, skill_level)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE skill_level = VALUES(skill_level)
    """, (employee_id, skill_id, skill_level))
    conn.commit()
    conn.close()

def get_all_skills_employee(employee_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT skill_id,skill_level FROM skills_to_employees WHERE employee_id = %s", (employee_id,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def update_skill_level(employee_id, skill_id, new_level):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE skills_to_employees
        SET skill_level = %s
        WHERE employee_id = %s AND skill_id = %s
    """, (new_level, employee_id, skill_id))
    conn.commit()
    conn.close()