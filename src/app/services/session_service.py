from fastapi import HTTPException, status
from src.database.session_repository import SessionRepository
from src.app.services.helpers.hash_password import hash_password
from src.app.services.helpers.verify_password import verify_password
from src.api.models.create_session_data import CreateSessionData
from src.api.models.join_session_data import JoinSessionData
from src.app.models.app_models import GameSession, User
from uuid import uuid4


class SessionService:
    def __init__(self, session_repository:SessionRepository):
        self._session_repository = session_repository

    def create_session(self, create_session_data: CreateSessionData, user:User) -> GameSession:
        password = create_session_data.password
        hashed_password = hash_password(password)
        new_session = GameSession(
            **{
                "id": str(uuid4()),
                "name": create_session_data.name,
                "password": hashed_password,
                "player_limit": create_session_data.player_cap,
                "admin": user.id
            }
        )
        self._session_repository.save_session_db(new_session,user)
        return new_session
            
    def delete_session(self, session_id, user:User):
        session = self._session_repository.get_session_from_id(session_id)
        if not session:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
                detail="Invalid session name",
                headers={"WWW-Authenticate": "Bearer"},
            )
        if session.admin != user.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only admin can delete sessions!",
                headers={"WWW-Authenticate": "Bearer"},
            )
        self._session_repository.delete_session_db(session=session)
        return {"message": f"{session.name} deleted successfully"}


    def join_session(self, session_id:str, join_session_data: JoinSessionData, user: User):
        session = self._session_repository.get_session_from_id(session_id)
        if not session:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
                detail="Invalid session name",
                headers={"WWW-Authenticate": "Bearer"},
            )
        user_sessions = self.show_user_sessions(user)

        if any(session["session_id"] == session_id for session in user_sessions["user_sessions"]):
            raise HTTPException(
                status_code=status.HTTP_200_OK,
                detail=f"Already in {session.name}",
                headers={"WWW-Authenticate": "Bearer"},
            )

        if not verify_password(plain_password=join_session_data.password, hashed_password=session.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Wrong password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        self._session_repository.join_user_to_session(user_id=user.id, session_id=session.id, role="player")
        return {"message": f"Joined {session.name} successfully"}


    def leave_session(self, session_id, user:User):
        session = self._session_repository.get_session_from_id(session_id)
        if not session:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
                detail="Invalid session name",
                headers={"WWW-Authenticate": "Bearer"},
            )
        self._session_repository.leave_user_from_session(user_id=user.id, session_id=session.id)
        if user.id == session.admin:
            self.delete_session(session_id, user)
            return {"message": f"Admin left session - session {session.name} deleted"}
        return {"message": f"Left {session.name} successfully"}


    
    def show_user_sessions(self, user:User):
        sessions = self._session_repository.get_user_session(user.id)
        return {"user_sessions": sessions}