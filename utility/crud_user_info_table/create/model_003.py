import sqlite3
import pandas as pd

def model(
    id_credential: int,
    name: str,
    email: str,
    phone: str,
    DB_NAME: str = "database.sqlite",
):
    connection = sqlite3.connect(f"{DB_NAME}")
    df = pd.read_sql_query(f"SELECT * FROM table_user_info;", connection)
    insert_columns = ["id_credential", "name", "email", "phone"]

    sql_query_insert_data = f"""
    INSERT INTO table_user_info (
        {", ".join(insert_columns)}
    ) VALUES (
        {", ".join(['?'] * len(insert_columns))}
    );
    """

    connection.execute(sql_query_insert_data, (id_credential, name, email, phone))
    connection.commit()
    connection.close()

    print("Inserted successfully")
