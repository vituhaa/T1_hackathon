from dbconnect import get_connection

"""CREATE TABLE Projects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT NOT NULL,
    project_name VARCHAR(100) NOT NULL,
    role VARCHAR(100),
    description VARCHAR(255),
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (employee_id) REFERENCES Employees(id) ON DELETE CASCADE
);
"""

def create_project(employee_id,project_name,role,description,start_date,end_date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Projects (employee_id,project_name,role,description,start_date,end_date)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (employee_id,project_name,role,description,start_date,end_date))
    conn.commit()
    cursor.close()
    conn.close()

def get_all_projects(employee_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Projects WHERE employee_id = %s", (employee_id,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result