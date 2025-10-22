from src.app.handlers.user_creation_handlers import UserCreationHandler, UserLoginHandler, GetCurrentUserHandler
from src.database.user_repository import UserRepository
from src.app.services.user_service import UserService
from fastapi import Request, Depends


def get_user_repository():
    return UserRepository()

def get_user_login_service(request: Request, user_repository: UserRepository = Depends(get_user_repository)):
    secret_key = request.app.state.config.secret_key
    return UserService(user_repository=user_repository, secret_key=secret_key)
    
def get_user_creation_service(request: Request, user_repository: UserRepository = Depends(get_user_repository)):
    secret_key = request.app.state.config.secret_key
    return UserService(user_repository=user_repository, secret_key=secret_key)

def get_current_user_service(request: Request, user_repository: UserRepository = Depends(get_user_repository)):
    secret_key = request.app.state.config.secret_key
    return UserService(user_repository=user_repository, secret_key=secret_key)


def user_creation_dependency(user_register_service: UserService = Depends(get_user_creation_service)):
    return UserCreationHandler(user_creation=user_register_service)

def login_dependency(user_login_service: UserService = Depends(get_user_login_service)):
    return UserLoginHandler(user_login=user_login_service)

def current_user_dependency(get_current_user_service: UserService = Depends(get_current_user_service)):
    return GetCurrentUserHandler(get_current_user=get_current_user_service)