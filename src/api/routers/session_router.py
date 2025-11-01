from fastapi import APIRouter, Depends
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer

from src.api.models.create_session_data import CreateSessionData
from src.api.models.join_session_data import JoinSessionData
from src.app.handlers.session_creation_handler import SessionCreationHandler
from src.app.handlers.join_session_handler import JoinSessionHandler
from src.app.handlers.leave_session_handler import LeaveSessionHandler
from src.app.handlers.delete_session_handler import DeleteSessionHandler
from src.app.handlers.show_user_sessions_handler import ShowUserSessionsHandler
from src.api.dependencies.dependencies import (get_session_creation_handler,get_join_session_handler,get_leave_session_handler,get_delete_session_handler,get_show_user_sessions_handler)


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")

@router.post("/sessions")
def create_session(
    session_data: CreateSessionData,
    token: Annotated[str, Depends(oauth2_scheme)],
    handler: SessionCreationHandler = Depends(get_session_creation_handler),
):
    return handler.handle(session_data=session_data, token=token)

@router.patch("/sessions/{session_id}/join_session") #patch
def join_session(
    token: Annotated[str, Depends(oauth2_scheme)],
    join_session_data: JoinSessionData,
    session_id = str,
    handler: JoinSessionHandler = Depends(get_join_session_handler),
):
    return handler.handle(session_id=session_id, join_session_data=join_session_data, token=token)

@router.patch("/sessions/{session_id}/leave_session")
def leave_session(
    token: Annotated[str, Depends(oauth2_scheme)],
    session_id = str,
    handler: LeaveSessionHandler = Depends(get_leave_session_handler),
):
    return handler.handle(session_id=session_id, token=token)

@router.delete("/sessions/{session_id}") #delete
def delete_session(
    token: Annotated[str, Depends(oauth2_scheme)],
    session_id = str,
    handler: DeleteSessionHandler = Depends(get_delete_session_handler),
):
    return handler.handle(session_id=session_id, token=token)

@router.get("/sessions")
def show_user_session(
    token: Annotated[str, Depends(oauth2_scheme)],
    handler: ShowUserSessionsHandler = Depends(get_show_user_sessions_handler),
):
    return handler.handle(token=token)