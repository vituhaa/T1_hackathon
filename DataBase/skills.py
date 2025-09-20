from dbconnect import get_connection

"""CREATE TABLE Skills (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    is_lang BOOLEAN DEFAULT FALSE,
    is_prog_lang BOOLEAN DEFAULT FALSE
);"""

def create_skill(name, is_lang=False, is_prog_lang=False):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Skills (name, is_lang, is_prog_lang)
        VALUES (%s, %s, %s)
    """, (name, is_lang, is_prog_lang))
    conn.commit()
    cursor.close()
    conn.close()



def get_skill(skill_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Skills WHERE id=%s", (skill_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def get_skill_id(name_skill):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM Skills WHERE name=%s", (name_skill,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def get_all_lang_skills():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM Skills WHERE is_lang = TRUE")
    result = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return result

def get_all_prog_skills():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM Skills WHERE is_prog_lang = TRUE")
    result = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return result

def get_all_skills():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Skills")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
