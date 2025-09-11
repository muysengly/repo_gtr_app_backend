import sqlite3

def model(
        username: str, 
        new_password: str, 
        DB_NAME="database.sqlite"):
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        cursor.execute("UPDATE table_credential SET password=? WHERE username=?",(new_password, username))
        connection.commit()
        connection.close()
        print("Updated successfully")
    except Exception as e:
        print("Error:", e)
