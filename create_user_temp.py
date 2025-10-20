import json
from pydantic import BaseModel


class User(BaseModel):
    id:int
    username:str
    email: str
    

def create_user(registered_user:dict[str, str]):
    with open("/workdir/src/database/users.json", "r") as file:
        users_list = json.load(file)
        user_id = users_list["users"][-1]["id"] + 1

        new_user = User(id=user_id,username=registered_user["username"],email=registered_user["email"])
        
        users_list["users"].append(new_user.__dict__)
        users_list["usernames"].append(new_user.username)

    with open("/workdir/src/database/users.json", "w") as db:
        json.dump(users_list,db, indent=4)


user_data = {
  "username": "Kuba",
  "email": "wiktor@email.com",
  "password": "Siema123#"
}
create_user(user_data)

