from src.app.services.session_service import SessionService
from src.api.models.session_data import SessionData



class SessionCreationHandler:
    def __init__(self, session_service: SessionService):
        self._session_service = session_service

    def handle(self, session_data: SessionData):
        return self._session_service.create_session(session_data)
