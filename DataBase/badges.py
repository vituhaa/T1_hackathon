from dbconnect import get_connection

"""CREATE TABLE Badges (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    points_reward INT DEFAULT 0
);
"""

def create_badge(name, description="no desc", points_reward=0):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Badges (name, description, points_reward)
        VALUES (%s, %s, %s)
    """, (name, description, points_reward))
    conn.commit()
    cursor.close()
    conn.close()

def get_points_by_id(id):
    """
    Возвращает очки опыта за это достижение
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT points_reward FROM Badges WHERE id=%s", (id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result