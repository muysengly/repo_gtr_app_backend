import sqlite3
from datetime import datetime

def model(
        username: str, 
        new_password: str, 
        DB_NAME: str=""):
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        datetime_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("UPDATE table_credential SET password=?, updated_at=? WHERE username=?", (new_password, datetime_now, username))
        connection.commit()
        connection.close()
        print("Updated successfully")
    except Exception as e:
        print("Error:", e)
