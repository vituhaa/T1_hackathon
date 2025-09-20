from dbconnect import get_connection

"""
CREATE TABLE Learning_courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    link VARCHAR(255),
    skill_id INT,
    FOREIGN KEY (skill_id) REFERENCES Skills(id) ON DELETE SET NULL
);
"""

def create_course(title, link, skill_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO learning_courses (title, link, skill_id)
        VALUES (%s, %s, %s)
    """, (title, link, skill_id))
    conn.commit()
    cursor.close()
    conn.close()

def get_courses_ids_by_skill_id(skill_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM learning_courses WHERE skill_id=%s", (skill_id,))
    result = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return result

