import sys
from pathlib import Path

project_root = Path(__file__).parent
sys.path.append(str(project_root))

from dbconnect import get_connection

"""CREATE TABLE Positions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_closed BOOLEAN DEFAULT FALSE
);"""

def create_position(name,description):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Positions (name,description)
        VALUES (%s, %s)
    """, (name,description))
    conn.commit()
    cursor.close()
    conn.close()

def get_all_positions(is_closed=True):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Positions WHERE is_closed = %s", (is_closed,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def close_position(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Positions SET is_closed = TRUE WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()

