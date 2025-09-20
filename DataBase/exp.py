import sys
from pathlib import Path

project_root = Path(__file__).parent
sys.path.append(str(project_root))

from dbconnect import get_connection

"""CREATE TABLE EXP (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT NOT NULL,
    exp INT DEFAULT 0,
    level INT DEFAULT 1,
    FOREIGN KEY (employee_id) REFERENCES Employees(id) ON DELETE CASCADE
);
"""

def create_exp_zero(employee_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO EXP (employee_id)
        VALUES (%s)
    """, (employee_id,))
    conn.commit()
    cursor.close()
    conn.close()

def get_exp(employee_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT exp FROM EXP WHERE employee_id=%s", (employee_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def update_exp(points, employee_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE EXP SET exp = exp + %s WHERE employee_id = %s", (points,employee_id))
    conn.commit()
    cursor.close()
    conn.close()

def update_lvl(employee_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE EXP SET level = level + 1 WHERE employee_id = %s", (employee_id,))
    conn.commit()
    cursor.close()
    conn.close()