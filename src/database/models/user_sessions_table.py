from sqlalchemy import Table, Column, String, ForeignKey
from src.database.database import metadata

user_sessions_table = Table(
    "user_sessions",
    metadata,
    Column("session_id", String, ForeignKey("session.id"), primary_key=True),
    Column("user_id", String, ForeignKey("user.id"), primary_key=True),
    Column("role", String)
)