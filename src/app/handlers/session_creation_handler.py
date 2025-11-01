from src.app.services.session_service import SessionService
from src.api.models.create_session_data import CreateSessionData
from src.app.services.user_service import UserService



class SessionCreationHandler:
    def __init__(self, session_service: SessionService, user_service: UserService):
        self._session_service = session_service
        self._user_service = user_service

    def handle(self, session_data: CreateSessionData, token:str):
        user = self._user_service.get_current_user(token=token)
        return self._session_service.create_session(session_data, user)
