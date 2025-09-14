import sqlite3
from datetime import datetime

def model(
    id_user_info: int,
    argkw: dict,
    DB_NAME: str = "database.sqlite",
):
    connection = sqlite3.connect(f"{DB_NAME}")
    table_name = "table_user_info"
    argkw["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    keys = list(argkw.keys())
    values = [argkw[key] for key in keys]

    sql_query_insert_data = f"""
    UPDATE {table_name} SET
        {", ".join([f"{key} = ?" for key in keys])}
    WHERE id = ?;
    """
    sql_query_insert_data

    connection.execute(sql_query_insert_data, (*values, id_user_info))
    connection.commit()
    connection.close()
    print("Updated successfully")
