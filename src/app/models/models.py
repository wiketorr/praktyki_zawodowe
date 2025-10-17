from pydantic import BaseModel


class User(BaseModel):  # We need a model that will represent user profile in the app.
    id: int
    username: str
    email: str
    user_sessions: list[int]
    user_characters: list[int]
