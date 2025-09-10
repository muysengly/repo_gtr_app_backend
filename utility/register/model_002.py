if __name__ == "__main__":

    import os
    import sys

    os.chdir("../../")
    sys.path.append(os.getcwd())

    print(os.getcwd())

    from utility.crud_cedential_table.create.model_001 import model as insert_credential

    def model(
        username: str,
        password: str,
        DB_NAME: str = "",
    ):

        if len(username) < 6:
            raise ValueError("Username must be at least 6 characters long")
        else:
            insert_credential(username, password, DB_NAME=DB_NAME)

    model("abc", "abc", DB_NAME="database.sqlite")


################################################################################

from utility.crud_cedential_table.create.model_001 import model as insert_credential


def model(
    username: str,
    password: str,
    DB_NAME: str = "",
):

    if len(username) < 6:
        raise ValueError("Username must be at least 6 characters long")
    else:
        insert_credential(username, password, DB_NAME=DB_NAME)
        print("User registered successfully")
