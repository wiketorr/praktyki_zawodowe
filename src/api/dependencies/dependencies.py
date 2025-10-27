from src.app.handlers.user_creation_handler import UserCreationHandler
from src.app.handlers.get_current_user_handler import GetCurrentUserHandler
from src.app.handlers.user_login_handler import UserLoginHandler
from src.database.user_repository import UserRepository
from src.app.services.user_service import UserService
from src.database.models.user_table import metadata
from fastapi import Request, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_user_repository():
    engine = create_engine("postgresql://devuser:devpass@db:5432/rpg_sim")
    metadata.create_all(bind=engine)
    SesionLocal = sessionmaker(bind=engine)
    session = SesionLocal()
    return UserRepository(session)


def get_user_service(
    request: Request, user_repository: UserRepository = Depends(get_user_repository)
):
    secret_key = request.app.state.config.secret_key
    return UserService(user_repository=user_repository, secret_key=secret_key)


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


