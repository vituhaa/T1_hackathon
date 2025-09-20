import sys
from pathlib import Path

project_root = Path(__file__).parent
sys.path.append(str(project_root))

from dbconnect import get_connection

"""CREATE TABLE Skills_required (
    id INT AUTO_INCREMENT PRIMARY KEY,
    position_id INT NOT NULL,
    skill_id INT NOT NULL,
    FOREIGN KEY (position_id) REFERENCES Positions(id) ON DELETE CASCADE,
    FOREIGN KEY (skill_id) REFERENCES Skills(id) ON DELETE CASCADE
);"""

def create_required_skill(position_id,skill_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Skills_required (position_id,skill_id)
        VALUES (%s, %s)
    """, (position_id,skill_id))
    conn.commit()
    cursor.close()
    conn.close()

def get_skills_required_for_position(position_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT skill_id FROM Skills_required WHERE position_id = %s", (position_id,))
    result = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return result

