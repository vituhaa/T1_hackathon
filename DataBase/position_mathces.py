import sys
from pathlib import Path

project_root = Path(__file__).parent
sys.path.append(str(project_root))

from dbconnect import get_connection

"""CREATE TABLE Position_matches (
    id INT AUTO_INCREMENT PRIMARY KEY,
    position_id INT NOT NULL,
    employee_id INT NOT NULL,
    match_score DECIMAL(5,2),
    FOREIGN KEY (position_id) REFERENCES Positions(id) ON DELETE CASCADE,
    FOREIGN KEY (employee_id) REFERENCES Employees(id) ON DELETE CASCADE
);"""

def create_match(position_id,employee_id,match_score):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Position_matches (position_id,employee_id,match_score)
        VALUES (%s, %s, %s)
    """, (position_id,employee_id,match_score))
    conn.commit()
    cursor.close()
    conn.close()

def get_match_score(position_id,employee_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT match_score FROM Position_matches WHERE position_id = %s AND employee_id = %s", (position_id,employee_id))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def get_all_matches(position_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT employee_id,match_score FROM Position_matches WHERE position_id = %s AND match_score <> 0", (position_id,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{"employee_id": row[0], "match_score": float(row[1])} for row in result]

