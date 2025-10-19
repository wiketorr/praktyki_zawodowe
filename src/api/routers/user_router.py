from fastapi import APIRouter

from ..models.register_data import RegisterData
from ...services.register_user import register_user


router = APIRouter()

@router.post("/user/register")
def register_user_endpoint(user_data: RegisterData):
    return register_user(user_data)