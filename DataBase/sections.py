from dbconnect import get_connection

"""CREATE TABLE Sections (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    fields TEXT
);"""

def create_section(name,fields):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Sections (name,fields)
        VALUES (%s, %s)
    """, (name,fields))
    conn.commit()
    cursor.close()
    conn.close()

def get_all_sections():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Sections")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_fields_of_section(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT fields FROM Sections WHERE id = %s", (id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def count_sections():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT COUNT(*) FROM Sections")
    count = cursor.fetchone()[0] 
    cursor.close()
    conn.close()
    return count