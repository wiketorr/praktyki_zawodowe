from src.app.handlers.user_creation_handler import UserCreationHandler
from src.app.handlers.get_current_user_handler import GetCurrentUserHandler
from src.app.handlers.user_login_handler import UserLoginHandler
from src.app.handlers.session_creation_handler import SessionCreationHandler
from src.app.handlers.join_session_handler import JoinSessionHandler
from src.app.handlers.leave_session_handler import LeaveSessionHandler
from src.app.handlers.delete_session_handler import DeleteSessionHandler
from src.app.handlers.show_user_sessions_handler import ShowUserSessionsHandler

from src.database.user_repository import UserRepository
from src.app.services.user_service import UserService

from src.database.session_repository import SessionRepository
from src.app.services.session_service import SessionService


from fastapi import Request, Depends


#repository

def get_user_repository(request: Request):
    session = request.app.state.db_session
    return UserRepository(session)

def get_session_repository(request: Request):
    session = request.app.state.db_session
    return SessionRepository(session)

#service
def get_user_service(request: Request, user_repository: UserRepository = Depends(get_user_repository)):
    secret_key = request.app.state.config.secret_key
    return UserService(user_repository=user_repository, secret_key=secret_key)

def get_session_service(session_repository: SessionRepository = Depends(get_session_repository)):
    return SessionService(session_repository=session_repository)

#user dependency
def get_user_creation_handler(
    user_register_service: UserService = Depends(get_user_service),
):
    return UserCreationHandler(user_service=user_register_service)


def get_login_handler(user_login_service: UserService = Depends(get_user_service)):
    return UserLoginHandler(user_service=user_login_service)


def get_current_user_handler(
    get_current_user_service: UserService = Depends(get_user_service),
):
    return GetCurrentUserHandler(user_service=get_current_user_service)

#session dependency
def get_session_creation_handler(
    register_session_service: SessionService = Depends(get_session_service),
    user_service: UserRepository = Depends(get_user_service)
):
    return SessionCreationHandler(session_service=register_session_service, user_service=user_service)


def get_join_session_handler(
    join_session_service: SessionService = Depends(get_session_service), 
    user_service: UserRepository = Depends(get_user_service)
):
    return JoinSessionHandler(session_service=join_session_service, user_service=user_service)

def get_leave_session_handler(
    leave_session_service: SessionService = Depends(get_session_service), 
    user_service: UserRepository = Depends(get_user_service)
):
    return LeaveSessionHandler(session_service=leave_session_service, user_service=user_service)

def get_delete_session_handler(
    delete_session_service: SessionService = Depends(get_session_service), 
    user_service: UserRepository = Depends(get_user_service)
):
    return DeleteSessionHandler(session_service=delete_session_service, user_service=user_service)

def get_show_user_sessions_handler(
    show_user_sessions_service: SessionService = Depends(get_session_service), 
    user_service: UserRepository = Depends(get_user_service)
):
    return ShowUserSessionsHandler(session_service=show_user_sessions_service, user_service=user_service)