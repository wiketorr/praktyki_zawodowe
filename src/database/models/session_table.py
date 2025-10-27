from sqlalchemy import Table, Column, Integer, String, MetaData, ARRAY, Boolean
from src.database.database import metadata

session_table = Table(
    "session",
    metadata,
    Column("id", String, primary_key=True),
    Column("name", String, unique=True,index=True),
    Column("password", String),
    Column("players_count", Integer, nullable=True, default=0),
    Column("players_id", ARRAY(String), nullable=True, default=[]),
    Column("is_active", Boolean, default=False)
)
