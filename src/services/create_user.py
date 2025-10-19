import json
from ..app.models.app_models import User


def create_user(registered_user:dict[str, str]):
    with open("/workdir/src/database/users.json", "r") as file:
        users_list = json.load(file)
        user_id = users_list["users"][-1]["id"] + 1

        new_user = User(id=user_id,username=registered_user["username"],email=registered_user["email"], password=registered_user["password"])
        users_list["users"].append(new_user.__dict__)
        users_list["usernames"].append(new_user.username)

    with open("/workdir/src/database/users.json", "w") as db:
        json.dump(users_list,db, indent=4)

    