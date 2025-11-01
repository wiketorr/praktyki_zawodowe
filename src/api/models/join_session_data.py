from pydantic import BaseModel

class JoinSessionData(BaseModel):
    password: str


