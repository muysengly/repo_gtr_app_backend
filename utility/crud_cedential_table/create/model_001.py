import sqlite3

def model(
    username: str,
    password: str,
    DB_NAME="",
):
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO table_credential (username, password) VALUES (?, ?)", (username, password))
        connection.commit()
        connection.close()
        print("Inserted successfully")
    except Exception as e:
        print("Error: ", e)
