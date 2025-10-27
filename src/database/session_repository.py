from src.app.models.app_models import Session
from src.database.models.session_table import session_table
from src.database.models.user_sessions_table import user_sessions
from sqlalchemy import func
from sqlalchemy.orm import Session
import sqlalchemy as sa

class SessionRepository:
    def __init__(self,db_session: Session):
        self._db_session = db_session

    def save_session_db(self, registered_session: Session) -> None:
        save_user_query = sa.insert(session_table).values(id = registered_session.id,name = registered_session.name,password = registered_session.password)
        self._db_session.execute(save_user_query)
        self._db_session.commit()

    def get_session_db(self, session_name:str) -> Session:
        get_session_query = sa.select(session_table).where(session_table.c.name == session_name)
        session_db = self._db_session.execute(get_session_query).fetchone()
        if not session_db:
            return None
        else:
            session_dict = dict(session_db._mapping)
            session = Session(**session_dict)
            return session

    def join_user_to_session(self, user_id:str, session_id:str, role:str):
        add_player_id_to_session_table_query = sa.update(session_table).where(session_table.c.id == session_id).values(players_id = func.array_append(session_table.c.players_id, user_id))
        increment_player_count_on_session_table_query = sa.update(session_table).where(session_table.c.id == session_id).values(players_count = session_table.c.players_count + 1)
        add_user_and_session_ids_to_user_session_query = sa.insert(user_sessions).values(session_id = session_id, user_id = user_id, role = role)
        
        self._db_session.execute(increment_player_count_on_session_table_query)
        self._db_session.execute(add_player_id_to_session_table_query)
        self._db_session.execute(add_user_and_session_ids_to_user_session_query)
        self._db_session.commit()

   



