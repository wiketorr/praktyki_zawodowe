from src.app.models.app_models import User
from src.database.models.user_table import user_table
from sqlalchemy.orm import Session
import sqlalchemy as sa



class UserRepository:
    def __init__(self,db_session: Session):
        self._db_session = db_session
        
    def save_user_db(self, registered_user: User) -> None:
        save_user_query = sa.insert(user_table).values(id = registered_user.id,username = registered_user.username,password = registered_user.password, email = registered_user.email)
        self._db_session.execute(save_user_query)
        self._db_session.commit()


    def get_user_db(self, input_username: str) -> User | None:
        get_user_query = sa.select(user_table).where(user_table.c.username == input_username)
        user_db = self._db_session.execute(get_user_query).fetchone()
        if not user_db:
            return None
        else:
            user_dict = dict(user_db._mapping)
            user = User(
                **user_dict
            )
            return user
