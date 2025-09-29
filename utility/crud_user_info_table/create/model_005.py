import sqlite3

def model(
    argkw: dict, 
    DB_NAME: str = "database.sqlite"
    ):
    conn = sqlite3.connect(DB_NAME)
    keys = list(argkw.keys())
    values = list(argkw.values())

    sql = f"INSERT INTO table_user_info ({', '.join(keys)}) VALUES ({', '.join(['?']*len(keys))})"
    conn.execute(sql, values)
    conn.commit()
    conn.close()
    print("Inserted successfully")