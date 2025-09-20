from dbconnect import get_connection

"""CREATE TABLE Lvl_rewards (
    id INT AUTO_INCREMENT PRIMARY KEY,
    lvl_achieved INT NOT NULL,
    description VARCHAR(255)
);"""

def create_lvl_reward(lvl_achieved,description):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Lvl_rewards (lvl_achieved,description)
        VALUES (%s,%s)
    """, (lvl_achieved,description))
    conn.commit()
    cursor.close()
    conn.close()

def get_reward_by_lvl(lvl):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Lvl_rewards WHERE lvl_achieved=%s", (lvl,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def update_reward_by_lvl(lvl,description):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Lvl_rewards SET description = %s WHERE lvl_achieved = %s", (description,lvl))
    conn.commit()
    cursor.close()
    conn.close()