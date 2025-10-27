from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql://devuser:devpass@db:5432/rpg_sim")
metadata = MetaData()

SesionLocal = sessionmaker(bind=engine)