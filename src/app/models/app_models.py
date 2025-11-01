from pydantic import BaseModel


class User(BaseModel):
    id: str
    username: str
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class GameSession(BaseModel):
    id: str
    name: str
    password: str
    player_limit: int
    admin: str
    player_count: int | None = None


class UserSessions(BaseModel):
    session_id: str
    name: str
    role: str