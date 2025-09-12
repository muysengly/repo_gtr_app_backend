from utility.crud_cedential_table.create.model_003 import model as create_credential


create_credential(
    argkw={
        "username": "admin004",
        "password": "admin004",
    },
    DB_NAME="database.sqlite",
)

from utility.crud_cedential_table.update.model_001 import model as update_credential
update_credential("young","ping","database.sqlite")  