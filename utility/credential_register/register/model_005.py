import random
import string
import sqlite3

def generate_verification_code(length=6):
    return ''.join(random.choices(string.digits, k=length))

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

        cursor.execute("""INSERT INTO table_user_info(id_credential, name, email, phone, telegram)VALUES (?, ?, ?, ?, ?)""",
            (id_credential, name, email, phone, telegram),)
        connection.commit()

        verification_code = generate_verification_code()
        print(f"User '{name}' registered successfully with email '{email}'")
        print(f"Verification code (send this via email/web): {verification_code}")

        return {
            "id_credential": id_credential,
            "email": email,
            "verification_code": verification_code  # ephemeral
        }

    except sqlite3.IntegrityError as e:
        print("Registration failed:", e)
        return None
    finally:
        connection.close()
