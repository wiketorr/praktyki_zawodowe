from pydantic import BaseModel


class User(BaseModel):
    id: str
    username: str
    email: str
    password: str
    user_sessions: list[str] | None = None
    user_characters: list[str] | None = None


class Token(BaseModel):
    access_token: str
    token_type: str


class GameSession(BaseModel):
    id: str
    name: str
    password: str
    player_count: int | None = None
    players_id: list[str] | None = None

