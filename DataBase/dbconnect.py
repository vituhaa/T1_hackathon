import sys
from pathlib import Path

project_root = Path(__file__).parent
sys.path.append(str(project_root))

import mysql.connector
import json

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",        # твой пользователь
        password="skdfkFE4320-PDK74k_=djfuJDjfk", # твой пароль
        database="hacaton"     # твоя база
    )

def get_all_as_json(table_name):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return json.dumps(rows, indent=4, ensure_ascii=False)