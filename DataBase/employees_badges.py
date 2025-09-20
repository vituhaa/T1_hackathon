import sys
from pathlib import Path

project_root = Path(__file__).parent
sys.path.append(str(project_root))

from dbconnect import get_connection

"""CREATE TABLE Employees_badges (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT NOT NULL,
    badge_id INT NOT NULL,
    points_reward INT DEFAULT 0,
    FOREIGN KEY (employee_id) REFERENCES Employees(id) ON DELETE CASCADE,
    FOREIGN KEY (badge_id) REFERENCES Badges(id) ON DELETE CASCADE
);"""

def create_employee_badge(employee_id, badge_id,points_reward):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Employees_badges (employee_id, badge_id, points_reward)
        VALUES (%s, %s, %s)
    """, (employee_id, badge_id, points_reward))
    conn.commit()
    cursor.close()
    conn.close()

def get_employees_badges(employee_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT badge_id FROM Employees_badges WHERE employee_id=%s", (employee_id,))
    result = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return result