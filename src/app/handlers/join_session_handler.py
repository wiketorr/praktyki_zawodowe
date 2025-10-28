from src.app.services.session_service import SessionService
from src.api.models.join_session_data import JoinSessionData


class JoinSessionHandler:
    def __init__(self, session_service: SessionService):
        self._session_service = session_service

    def handle(self, join_session_data: JoinSessionData, token:str):
        return self._session_service.join_session(join_session_data,token)
