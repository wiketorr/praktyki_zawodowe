from sqlalchemy import Table, Column, Integer, String, MetaData, ARRAY


metadata = MetaData()

user_table = Table(
    "user",
    metadata,
    Column("id", String, primary_key=True),
    Column("username", String, unique=True, index=True),
    Column("password", String),
    Column("email", String),
    Column("user_sessions", ARRAY(Integer), nullable=True, default=[]),
    Column("user_characters", ARRAY(Integer), nullable=True, default=[]),
)
