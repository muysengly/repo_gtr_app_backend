import sqlite3


def model(
    DB_NAME: str = "",
):

    connection = sqlite3.connect(f"{DB_NAME}")
    cursor = connection.cursor()

    sql_query_for_reading = "SELECT * FROM table_credential;"

    cursor.execute(sql_query_for_reading)

    results = cursor.fetchall()

    results = [list(row) for row in results]

    connection.close()
    return results
