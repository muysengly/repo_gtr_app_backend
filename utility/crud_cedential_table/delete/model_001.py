# TODO: delete based on id
import sqlite3


def model(
    cre_id: str,
    DB_NAME: str = "",
):
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM table_credential WHERE id=?", (cre_id,))
        connection.commit()
        connection.close()
        print("Deleted successfully")
    except Exception as e:
        print("Error: ", e)
