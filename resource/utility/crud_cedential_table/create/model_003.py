import sqlite3

def model(
    argkw: dict,
    DB_NAME: str = "database.sqlite",
):

    connection = sqlite3.connect(f"{DB_NAME}")
    table_name = "table_credential"

    keys = list(argkw.keys())

    values = [argkw[key] for key in keys]

    sql_query_insert_data = f"""
    INSERT INTO {table_name} (
        {", ".join(keys)}
    ) VALUES (
        {", ".join(['?'] * len(keys))}
    );
    """

    sql_query_insert_data

    connection.execute(sql_query_insert_data, (*values,))
    connection.commit()

    connection.close()
    print("Inserted successfully")
