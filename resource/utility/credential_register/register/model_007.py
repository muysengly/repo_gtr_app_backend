import sqlite3
import random
import re
def register_user(argkw, DB_PATH="database.sqlite"):
    username, password = argkw.get("username"), argkw.get("password")
    if not (username and password):
        raise ValueError("Username and password are required")
    
    # Username: 8+ chars, 1 uppercase, no Khmer chars
    if (len(username) < 8 or not any(c.isupper() for c in username) or 
        re.search(r'[\u1780-\u17FF]', username)):
        raise ValueError("True")
    
    # Password: 8+ chars, number, @/$, no spaces
    if (len(password) < 8 or not any(c.isdigit() for c in password) or 
        not any(c in "@$" for c in password) or ' ' in password):
        raise ValueError("True")
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        if cur.execute("SELECT 1 FROM table_credential WHERE username=?", (username,)).fetchone():
            print("Username already exists")
            return None
        cur.execute("INSERT INTO table_credential (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
    finally:
        conn.close()
    print(f"Register Success! Verification code: {''.join(random.choices('0123456789', k=6))}")
