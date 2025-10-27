from pydantic import BaseModel,Field
from enum import Enum

class SessionRoleEnum(str, Enum):
    gamemaster = "gamemaster"
    player = "player"

class JoinSessionData(BaseModel):
    name: str = Field(min_length=4)
    password: str
    role: SessionRoleEnum = SessionRoleEnum.player