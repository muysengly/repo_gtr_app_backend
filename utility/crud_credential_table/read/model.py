import os
import sqlite3

connection = sqlite3.connect("../database.sqlite")

def model(username, password):
    cursor = connection.cursor()
    cursor.execute("SELECT credential_id FROM table_credential WHERE username=? AND password=?", (username, password))
    credentail = cursor.fetchall()
    if not credentail:
        return False
connection.close()
