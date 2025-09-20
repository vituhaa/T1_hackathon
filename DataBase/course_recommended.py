import sys
from pathlib import Path

project_root = Path(__file__).parent
sys.path.append(str(project_root))

from dbconnect import get_connection

"""
CREATE TABLE Course_recommended (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT NOT NULL,
    course_id INT NOT NULL,
    is_achieved BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (employee_id) REFERENCES Employees(id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES Learning_courses(id) ON DELETE CASCADE
);
"""

def create_recommendation(employee_id, course_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO course_recommended (employee_id, course_id)
        VALUES (%s, %s)
    """, (employee_id, course_id))
    conn.commit()
    cursor.close()
    conn.close()

def get_course_id_by_recom_id(employee_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT course_id FROM course_recommended WHERE employee_id=%s", (employee_id,))
    result = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return result

def update_achieved(employee_id,course_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE course_recommended
        SET is_achieved = 1
        WHERE employee_id = %s AND course_id = %s
    """, (employee_id, course_id))
    conn.commit()
    cursor.close()
    conn.close()