from sqlalchemy import Table, Column, String, ARRAY
from src.database.database import metadata

user_table = Table(
    "user",
    metadata,
    Column("id", String, primary_key=True),
    Column("username", String, unique=True, index=True),
    Column("password", String),
    Column("email", String),
    Column("user_sessions", ARRAY(String), nullable=True, default=[]),
    Column("user_characters", ARRAY(String), nullable=True, default=[])
)
