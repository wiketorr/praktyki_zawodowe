from pydantic import BaseModel


class User(BaseModel):
    id: str
    username: str
    email: str
    password: str
    user_sessions: list[int] | None = None
    user_characters: list[int] | None = None


class Token(BaseModel):
    access_token: str
    token_type: str
