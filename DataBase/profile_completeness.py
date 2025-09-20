from dbconnect import get_connection

"""CREATE TABLE Profile_completeness (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT NOT NULL,
    section_id INT NOT NULL,
    is_completed BOOLEAN DEFAULT FALSE,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    data_json TEXT,
    FOREIGN KEY (employee_id) REFERENCES Employees(id) ON DELETE CASCADE
);
"""

def create_profile_completeness(employee_id,section_id,data_json):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Profile_completeness (employee_id,section_id,data_json)
        VALUES (%s, %s, %s)
    """, (employee_id,section_id,data_json))
    conn.commit()
    cursor.close()
    conn.close()

def update_section_data(employee_id,section_id,data_json,last_updated,is_completed=False):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Profile_completeness
        SET data_json = %s,
            is_completed = %s,
            last_updated = %s
        WHERE employee_id = %s AND section_id = %s
    """, (data_json,is_completed,last_updated,employee_id,section_id))
    conn.commit()
    cursor.close()
    conn.close()

def count_completed_sections(employee_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        SELECT COUNT(*)
        FROM Profile_completeness
        WHERE employee_id = %s AND is_completed = TRUE
    """
    cursor.execute(query, (employee_id,))
    count = cursor.fetchone()[0] 
    cursor.close()
    conn.close()
    return count
