from pydantic import BaseModel
from uuid import uuid4, UUID

class User(BaseModel):  # We need a model that will represent user profile in the app.
    id: UUID = uuid4()
    username: str
    email: str
    password: str
    user_sessions: list[int] | None = None
    user_characters: list[int] | None = None
