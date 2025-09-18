import sqlite3

def model(
    id_credential: int,
    name: str,
    email: str,
    phone: str,
    DB_NAME: str = "database.sqlite",
):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    sql_query_insert_data = "INSERT INTO table_user_info (id_credential, name, email, phone) VALUES (?, ?, ?, ?)"

    try:
        cursor.execute(sql_query_insert_data, (id_credential, name, email, phone))
        connection.commit()
        print("Inserted successfully")
    except sqlite3.IntegrityError:
        # This happens if a UNIQUE constraint fails (e.g., duplicate username)
        print("username already done!")
    finally:
        connection.close()
