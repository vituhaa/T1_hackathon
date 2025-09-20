from dbconnect import get_connection

"""CREATE TABLE Employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    fath_name VARCHAR(100),
    email VARCHAR(100) UNIQUE
);"""

# CREATE
def create_employee(first_name, last_name, fath_name, email):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO Employees (first_name, last_name, fath_name, email)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (first_name, last_name, fath_name, email))
    conn.commit()
    cursor.close()
    conn.close()

# READ
def get_employee(employee_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)  # dictionary=True - получаем dict
    cursor.execute("SELECT * FROM Employees WHERE id = %s", (employee_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result





