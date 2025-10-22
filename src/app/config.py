from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal
from pydantic import Field

class Config(BaseSettings):
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = Field(
        default="INFO"
    )
    secret_key: str