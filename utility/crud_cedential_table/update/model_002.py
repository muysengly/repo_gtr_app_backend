import sqlite3

def model(
        username: str, 
        new_password: str, 
        DB_NAME="",
    ):
    try:
        with sqlite3.connect(DB_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE table_credential SET password=? WHERE username=?", (new_password, username))
            connection.commit()
            print("Updated successfully")
    except Exception as e:
        print("Error:", e)
