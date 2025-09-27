import sqlite3
if __name__ == "__main__":
    import os
    import sys

    os.chdir("../../")
    sys.path.append(os.getcwd())
    print(os.getcwd())

def register_email(
    email: str,
    password: str,
    name: str,
    phone: str,
    telegram: str,
    DB_NAME: str = "database.sqlite",
):
    if len(email) < 6:
        raise ValueError("Email must be at least 6 characters long")
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    try:
        cursor.execute("INSERT INTO table_credential (username, password) VALUES (?, ?)",
                       (email, password),)
        id_credential = cursor.lastrowid
        cursor.execute("INSERT INTO table_user_info (id_credential, name, email, phone,telegram) VALUES (?, ?, ?, ? ,?)",
                       (id_credential, name, email, phone, telegram),)
        connection.commit()

        print(f"User '{name}' registered successfully with email '{email}'")
        return {"id_credential": id_credential, "email": email}
    except sqlite3.IntegrityError as e:
        print("Registration failed:", e)
        return None
    finally:
        connection.close()
