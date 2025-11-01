from src.app.models.app_models import GameSession
from src.database.models.session_table import session_table
from src.database.models.user_sessions_table import user_sessions_table
from src.app.models.app_models import User
from sqlalchemy.orm import Session
import sqlalchemy as sa



class SessionRepository:
    def __init__(self,db_session: Session):
        self._db_session = db_session

    def save_session_db(self, registered_session: GameSession, user:User) -> None:
        if self.get_session_from_id(registered_session.name):
            raise ValueError("session name is taken")
        save_session_query = sa.insert(session_table).values(id = registered_session.id, name = registered_session.name, password = registered_session.password, admin = user.id, player_limit = registered_session.player_limit)
        self._db_session.execute(save_session_query)
        self._db_session.commit()
        self.join_user_to_session(user_id=user.id, session_id=registered_session.id, role="gamemaster")

    def delete_session_db(self, session: GameSession) -> None:
        delete_session_query = sa.delete(session_table).where(session_table.c.id == session.id)
        self._db_session.execute(delete_session_query)
        self._db_session.commit()

    def join_user_to_session(self, user_id:str, session_id:str, role:str):
        increment_player_count_on_session_table_query = sa.update(session_table).where(session_table.c.id == session_id).values(players_count = session_table.c.players_count + 1)
        add_user_and_session_ids_to_user_session_query = sa.insert(user_sessions_table).values(session_id = session_id, user_id = user_id, role = role)
        
        self._db_session.execute(increment_player_count_on_session_table_query)
        self._db_session.execute(add_user_and_session_ids_to_user_session_query)
        self._db_session.commit()
        
    
    def leave_user_from_session(self,user_id:str, session_id:str):
        delete_user_from_user_session_query = sa.delete(user_sessions_table).where(user_sessions_table.c.user_id == user_id)
        self._db_session.execute(delete_user_from_user_session_query)
        self._db_session.commit()


    def get_user_session(self, user_id:str):
        search_for_users_sessions_in_user_sessions_table_query = sa.select(
            user_sessions_table.c.session_id,
            session_table.c.name,
            user_sessions_table.c.role
        ).join(
            session_table, user_sessions_table.c.session_id == session_table.c.id
        ).where(
            user_sessions_table.c.user_id == user_id 
        )
        user_sessions_db = self._db_session.execute(search_for_users_sessions_in_user_sessions_table_query)
        rows = user_sessions_db.fetchall()
        if not user_sessions_db:
            return None
        else:
            user_sessions_list = [dict(row._mapping) for row in rows]
            return user_sessions_list
        
    def get_session_from_id(self, session_id:str) -> GameSession:
        get_session_query = sa.select(session_table).where(session_table.c.id == session_id)
        session_db = self._db_session.execute(get_session_query).fetchone()
        if not session_db:
            return None
        else:
            session_dict = dict(session_db._mapping)
            session = GameSession(**session_dict)
            return session
