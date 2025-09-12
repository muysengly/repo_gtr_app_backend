import sqlite3

def model(
        id_credential:int,
        DB_PATH: str="database.sqlite"):
    try:
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM table_user_info WHERE id_credential=?", (id_credential,))
        connection.commit()
        connection.close()
        print("Deleted successfully")
    except Exception as e:
        print("Error:", e)