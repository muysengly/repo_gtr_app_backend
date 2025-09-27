# from utility.crud_cedential_table.delete.model_001 import model as delete_credential
# delete_credential(
#     cre_id="13",
#     DB_NAME="database.sqlite",
# )

# from utility.crud_user_info_table.create.model_004 import model 
# model(
#     id_credential=18,
#     name="Leap Heng",
#     email="Heng@123",
#     phone="0969345623",
#     DB_NAME="database.sqlite"
# )


# from utility.crud_cedential_table.create.model_001 import model as create_credential
 
# create_credential("heng","heng097","database.sqlite")  


# from utility.crud_user_info_table.delete.model_001 import model as delete_credential
# delete_credential("1","database.sqlite")  

# from utility.crud_user_info_table.update.model_001 import model as update_user_info
# update_user_info(
#     id_user_info = 4,
#     argkw={
#         "phone": "97560338",
#         "telegram": "xxx"
#     },
#     DB_NAME="database.sqlite"
# )

# from utility.crud_user_info_table.read.model_001 import model as read_user_info
# read_user_info(DB_NAME="database.sqlite")


# from utility.credential_login.login.model_001 import model_001 as credential_login
# credential_login(
#     username="vengey",
#     password="veng123",
#     DB_NAME="database.sqlite"
# )



# from utility.crud_cedential_table.update.model_001 import model as update_credential
# update_credential("heng","pong123","database.sqlite")


# from utility.credential_register.register.model_003 import register
# register(
#     username="vengey",
#     password="veng123",
#     name="Yu Veng",
#     email="yu@123",
#     phone="098765443",
#     DB_NAME="database.sqlite"
# )


# from utility.credential_login.login.model_001 import model_001 as credential_login
# credential_login(
#     username="admin123",
#     password="admin12345",
#     DB_NAME="database.sqlite"
# )


from utility.credential_register.register.model_004 import register_email
if __name__ == "__main__":
    user = register_email(
    email="jaker@example.com",
    password="mypassword123",
    name="jake Don",
    phone="0123456789",
    telegram="@jakerdon",
    DB_NAME="database.sqlite"
)
print("Returned data:", user)

 



