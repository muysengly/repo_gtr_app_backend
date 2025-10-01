import sqlite3
from datetime import datetime

def model_001(
    username: str, 
    password: str, 
    DB_NAME: str = "database.sqlite"
):
    connection = sqlite3.connect(f"{DB_NAME}")
    table_name = "table_credential"
    
    sql_query = f"""SELECT * FROM {table_name}
    WHERE username = ? AND password = ?
    LIMIT 1;"""

    cur = connection.cursor()
    cur.execute(sql_query, (username, password))
    user = cur.fetchone()
    connection.close()

    if user:
        print("Login successful")
        return True
    else:
        print(" Invalid username or password")
        return False
