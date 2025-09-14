# from utility.crud_cedential_table.delete.model_001 import model as delete_credential
# delete_credential(
#     cre_id="13",
#     DB_NAME="database.sqlite",
# )

# from utility.crud_user_info_table.delete.model_001 import model as delete_credential
# delete_credential("1","database.sqlite")  

from utility.crud_user_info_table.update.model_001 import model as update_user_info
update_user_info(
    id_user_info = 4,
    argkw={
        "phone": "97560338",
        "telegram": "xxx"
    },
    DB_NAME="database.sqlite"
)


