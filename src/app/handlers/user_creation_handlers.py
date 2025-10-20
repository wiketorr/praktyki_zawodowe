from ..services.user_service import UserService
from ...api.models.register_data import RegisterData
from pydantic import BaseModel


class UserCreationHandler():
    def __init__(self, user_service: UserService):
        self._user_service = user_service
    
    def handle(self, register_data: RegisterData):
        self._user_service.register_user(register_data)