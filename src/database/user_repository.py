import json
from src.app.models.app_models import User


class UserRepository:
    def save_user(self, registered_user: User) -> None:
        users_list = self._get_user_list()

        users_list[registered_user.username] = registered_user.model_dump(mode="json")

        with open("/workdir/src/database/users.json", "w") as db:
            json.dump(users_list, db, indent=4)

        return None

    def get_user(self, username: str) -> User | None:
        users_list = self._get_user_list()
        try:
            user = users_list[username]
            return User(**user)
        except KeyError:
            return None

    def _get_user_list(self) -> dict:
        with open("/workdir/src/database/users.json", "r") as file:
            return json.load(file)
