from fastapi import APIRouter, HTTPException

from ..models.register_data import RegisterData
from ...app.handlers.user_creation_handlers import UserCreationHandler
from src.database.user_repository import UserRepository
from src.app.services.user_service import UserService

router = APIRouter()

repository = UserRepository()
service = UserService(repository)
handler = UserCreationHandler(service)

@router.post("/user/register")
def register_user_endpoint(register_data: RegisterData):
    try:
        handler.handle(register_data)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))