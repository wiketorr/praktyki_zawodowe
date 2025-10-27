from src.app.handlers.user_creation_handler import UserCreationHandler
from src.app.handlers.get_current_user_handler import GetCurrentUserHandler
from src.app.handlers.user_login_handler import UserLoginHandler
from src.app.handlers.session_creation_handler import SessionCreationHandler
from src.app.handlers.join_session_handler import JoinSessionHandler

from src.database.user_repository import UserRepository
from src.app.services.user_service import UserService

from src.database.session_repository import SessionRepository
from src.app.services.session_service import SessionService

from src.database.database import SesionLocal

from fastapi import Request, Depends


#repository

def get_user_repository():
    session = SesionLocal()
    return UserRepository(session)

def get_session_repository():
    session = SesionLocal()
    return SessionRepository(session)

#service
def get_user_service(request: Request, user_repository: UserRepository = Depends(get_user_repository)):
    secret_key = request.app.state.config.secret_key
    return UserService(user_repository=user_repository, secret_key=secret_key)

def get_session_service(session_repository: SessionRepository = Depends(get_session_repository), user_service: UserRepository = Depends(get_user_service)):
    return SessionService(session_repository=session_repository, user_service=user_service)

#user dependency
def get_user_creation_dependency(
    user_register_service: UserService = Depends(get_user_service),
):
    return UserCreationHandler(user_service=user_register_service)


def get_login_dependency(user_login_service: UserService = Depends(get_user_service)):
    return UserLoginHandler(user_service=user_login_service)


def get_current_user_dependency(
    get_current_user_service: UserService = Depends(get_user_service),
):
    return GetCurrentUserHandler(user_service=get_current_user_service)

#session dependency
def get_session_creation_dependency(
    register_session_service: SessionService = Depends(get_session_service)
):
    return SessionCreationHandler(session_service=register_session_service)


def get_join_session_dependency(
    join_session_service: SessionService = Depends(get_session_service)
):
    return JoinSessionHandler(session_service=join_session_service)