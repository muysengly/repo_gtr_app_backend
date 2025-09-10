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

        insert_credential(username, password, DB_NAME=DB_NAME)


from utility.crud_cedential_table.create.model_001 import model as insert_credential


def model(
    username: str,
    password: str,
    DB_NAME: str = "",
):
    insert_credential(username, password, DB_NAME=DB_NAME)
