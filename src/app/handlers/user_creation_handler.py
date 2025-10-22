from src.app.services.user_service import UserService
from src.api.models.user_data import RegisterData


class UserCreationHandler:
    def __init__(self, user_service: UserService):
        self._user_service = user_service

    def handle(self, register_data: RegisterData):
        return self._user_service.register_user(register_data)
