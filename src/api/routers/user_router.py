from fastapi import APIRouter, HTTPException, Depends
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


from src.api.models.user_data import RegisterData
from src.app.handlers.user_creation_handlers import UserCreationHandler, UserLoginHandler, GetCurrentUserHandler
from src.api.dependencies.dependencies import user_creation_dependency, login_dependency, current_user_dependency

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")

@router.post("/user/register")
def register_user_endpoint(register_data: RegisterData, handler: UserCreationHandler = Depends(user_creation_dependency)):
    try:
        return handler.handle(register_data)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))
    


@router.post("/user/login")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], handler: UserLoginHandler = Depends(login_dependency)):
    return handler.handle(form_data)

@router.get("/user/me")
def read_users_me(token: Annotated[str, Depends(oauth2_scheme)], handler: GetCurrentUserHandler = Depends(current_user_dependency)):
    return handler.handle(token)