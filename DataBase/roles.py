from dbconnect import get_connection

"""CREATE TABLE Roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);"""

def create_role(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Roles (name)
        VALUES (%s)
    """, (name,))
    conn.commit()
    cursor.close()
    conn.close()

def get_role(role_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Roles WHERE id=%s", (role_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def get_role_id(name_role):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM Roles WHERE name=%s", (name_role,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def get_all_roles():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Roles")
    result =  cursor.fetchall()
    cursor.close()
    conn.close()
    return result
