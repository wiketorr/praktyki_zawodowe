from fastapi import APIRouter, Depends
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer

from src.api.models.session_data import SessionData
from src.api.models.join_session_data import JoinSessionData
from src.app.handlers.session_creation_handler import SessionCreationHandler
from src.app.handlers.join_session_handler import JoinSessionHandler
from src.api.dependencies.dependencies import (get_session_creation_dependency,get_join_session_dependency)


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")

@router.post("session/create_session")
def create_session(
    session_data: SessionData,
    token: Annotated[str, Depends(oauth2_scheme)],
    handler: SessionCreationHandler = Depends(get_session_creation_dependency),
):
    return handler.handle(session_data=session_data)

@router.get("session/join_session")
def join_session(
    token: Annotated[str, Depends(oauth2_scheme)],
    join_session_data: JoinSessionData,
    handler: JoinSessionHandler = Depends(get_join_session_dependency),
):
    return handler.handle(join_session_data=join_session_data, token=token)