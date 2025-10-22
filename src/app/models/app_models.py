from pydantic import BaseModel
from uuid import uuid4, UUID




class User(BaseModel):
    id: UUID = uuid4()
    username: str
    email: str
    password: str
    user_sessions: list[int] | None = None
    user_characters: list[int] | None = None

class Token(BaseModel):
    access_token: str
    token_type: str




