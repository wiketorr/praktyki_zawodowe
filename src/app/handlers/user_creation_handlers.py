from src.app.services.user_service import UserService
from src.api.models.user_data import RegisterData

from fastapi.security import OAuth2PasswordRequestForm


class UserCreationHandler():
    def __init__(self, user_creation: UserService):
        self._user_creation = user_creation
    
    def handle(self, register_data: RegisterData):
        return self._user_creation.register_user(register_data)

class UserLoginHandler():
    def __init__(self,user_login: UserService):
        self._user_login = user_login

    def handle(self,form_data: OAuth2PasswordRequestForm):
        return self._user_login.login_for_access_token(form_data)

class GetCurrentUserHandler():
    def __init__ (self,get_current_user: UserService):
        self._get_current_user = get_current_user
    
    def handle(self, token: str):
        return self._get_current_user.get_current_user(token)