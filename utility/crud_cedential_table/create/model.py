import sqlite3
from datetime import datetime

DB_NAME = "../database.sqlite"
conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()
now = datetime.now()

def create_cre(username, password):
    cur.execute(
        "INSERT INTO table_credential ( username, password) VALUES (?, ?)",
        (username, password)
    )
    conn.commit()
    conn.close()