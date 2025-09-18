import sqlite3

if __name__ == "__main__":

    import os
    import sys

    os.chdir("../../")
    sys.path.append(os.getcwd())

    print(os.getcwd())

def register(
    username: str,
    password: str,
    name: str,
    email: str,
    phone: str,
    DB_NAME: str = "database.sqlite",
):
    if len(username) < 6:
        raise ValueError("Username must be at least 6 characters long")

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    try:
        cursor.execute("INSERT INTO table_credential (username, password) VALUES (?, ?)",
                       (username, password),)
        id_credential = cursor.lastrowid

        cursor.execute("INSERT INTO table_user_info (id_credential, name, email, phone) VALUES (?, ?, ?, ?)",
                        (id_credential, name, email, phone),
        )

        connection.commit()
        print("User registered successfully")

    except sqlite3.IntegrityError as e:
        print("Registration failed:", e)

    finally:
        connection.close()