import os
import sys
import sqlite3
import pathlib

def get_connection():
    return sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../firststep.db")))

def login_user(username, password):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute("SELECT credential_id FROM table_credential WHERE username=? AND password=?", (username, password))
        cred = c.fetchone()
        if not cred:
            return False
        c.execute("SELECT student_id, student_name, student_phone FROM table_user_into_1 WHERE credential_id=?", (cred[0],))
        profile = c.fetchone()
        if not profile:
            return False
        print(f"✅ User '{username}' logged in!\n   Student ID: {profile[0]}\n   Name: {profile[1]}\n   Phone: {profile[2]}")
        return True

login_user("ping", "pass123")