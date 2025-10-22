from src.app.services.user_service import UserService


class GetCurrentUserHandler:
    def __init__(self, user_service: UserService):
        self._user_service = user_service

    def handle(self, token: str):
        return self._user_service.get_current_user(token)
