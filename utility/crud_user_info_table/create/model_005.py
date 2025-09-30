import sqlite3

def model(
    argkw: dict, 
    DB_NAME: str = "database.sqlite"):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    if cur.execute("SELECT 1 FROM table_user_info WHERE email=?", (argkw.get("email"),)).fetchone():
        print("Email exists!")
        conn.close()
        return
    
    cur.execute(f"INSERT INTO table_user_info ({', '.join(argkw)}) VALUES ({', '.join('?'*len(argkw))})",
        tuple(argkw.values()))
    conn.commit()
    conn.close()
    print("Inserted")
