from fastapi.security import OAuth2PasswordRequestForm
from src.app.services.user_service import UserService


class UserLoginHandler:
    def __init__(self, user_service: UserService):
        self._user_service = user_service

    def handle(self, form_data: OAuth2PasswordRequestForm):
        return self._user_service.login_for_access_token(form_data)
