import random
import string
import sqlite3

def generate_verification_code(length=6):
    return ''.join(random.choices(string.digits, k=length))

def register_email(
        argkw: dict, 
        DB_PATH: str = "database.sqlite" 
    ):
    if "email" not in argkw or len(argkw["email"]) < 6:
        raise ValueError("least 6 characters long")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    try:
        cur.execute("SELECT 1 FROM table_credential WHERE username=?", (argkw["username"],))
        if cur.fetchone():
            print("Username already exists!")
            return None

        cur.execute("INSERT INTO table_credential (username,password) VALUES (?,?)",
                    (argkw["username"], argkw["password"]))
        id_cred = cur.lastrowid

        cur.execute("INSERT INTO table_user_info (id_credential,name,email,phone,telegram) VALUES (?,?,?,?,?)",
                    (id_cred, argkw["name"], argkw["email"], argkw["phone"], argkw["telegram"]))
        conn.commit()

        code = generate_verification_code()
        return {"Register Success"}
    except sqlite3.IntegrityError as e:
        print("Registration failed:", e)
        return None
    finally:
        conn.close()
