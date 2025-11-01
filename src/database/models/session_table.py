from sqlalchemy import Table, Column, Integer, String, Boolean, ForeignKey
from src.database.database import metadata

session_table = Table(
    "session",
    metadata,
    Column("id", String, primary_key=True),
    Column("name", String, unique=True,index=True),
    Column("password", String),
    Column("admin", String, ForeignKey("user.id")),
    Column("player_limit",Integer, default=5),
    Column("players_count", Integer, nullable=True, default=0),
    Column("is_active", Boolean, default=False),  
)
