from fastapi import HTTPException, status
from src.database.session_repository import SessionRepository
from src.app.services.user_service import UserService
from src.api.models.session_data import SessionData
from src.api.models.join_session_data import JoinSessionData
from src.app.models.app_models import GameSession
from uuid import uuid4


class SessionService:
    def __init__(self, session_repository:SessionRepository, user_service: UserService):
        self._session_repository = session_repository
        self._user_service = user_service

    def create_session(self, session_data: SessionData) -> GameSession:
        password = session_data.password
        hashed_password = self._user_service.hash_password(password)
        new_session = GameSession(
            **{
                "id": str(uuid4()),
                "name": session_data.name,
                "password": hashed_password,
            }
        )
        self._session_repository.save_session_db(new_session)
        return new_session
    
    def _authenticate_session_join(self, session_name, session_password):
        session = self._session_repository.get_session_db(session_name)
        if not session:
            return False
        else:
            if not self._user_service.verify_password(plain_password=session_password, hashed_password=session.password):
                return False
        return session
            

    def join_session(self, join_session_data: JoinSessionData, token:str):
        session = self._authenticate_session_join(join_session_data.name, join_session_data.password)
        if not session:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid password or name",
                headers={"WWW-Authenticate": "Bearer"},
            )
        user = self._user_service.get_current_user(token=token)
        self._session_repository.join_user_to_session(user_id=user.id, session_id=session.id, role=join_session_data.role)
        return {"message": f"Joined {session.name} succesfully"}

        
    

