from ...database.user_repository import UserRepository
from src.api.models.register_data import RegisterData
from src.app.models.app_models import User

import hashlib

class UserService():
    def __init__(self, user_repository: UserRepository):
        self._user_repoistory = user_repository

    def _hash_password(self,password: str) -> str:
        hash = hashlib.new("SHA384")
        hash.update(password.encode())
        return hash.hexdigest()


    def register_user(self,user_data: RegisterData) -> User:
        if self._user_repoistory.get_user(user_data.username):
            raise ValueError("Username already taken")
        password = user_data.password
        hashed_password = self._hash_password(password)
        new_user = User(
            **{
            "username": user_data.username,
            "email": user_data.email,
            "password": hashed_password
            }
        )
        self._user_repoistory.save_user(new_user)
        return new_user