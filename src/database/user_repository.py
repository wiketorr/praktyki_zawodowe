import json
from src.app.models.app_models import User
import sqlalchemy as sa
from src.database.models.user_table import metadata, user_table

engine = sa.create_engine("postgresql://devuser:devpass@db:5432/rpg_sim")

metadata.create_all(bind=engine)

with engine.connect() as conn:
    result = conn.execute(sa.select(user_table))
    rows = result.fetchall()
    for row in rows:
        print(row)

class UserRepository:

    def save_user_db(self, registerd_user: User) -> None:
        print('siema')
        query = sa.insert(user_table).values(id = str(registerd_user.id),username = registerd_user.username,password = registerd_user.password, email = registerd_user.email)
        print('siema2')
        with engine.connect() as conn:
            conn.execute(query)
            conn.commit  
        print('siema3')
    def save_user(self, registered_user: User) -> None:
        users_list = self._get_user_list()

        users_list[registered_user.username] = registered_user.model_dump(mode="json")

        with open("/workdir/src/database/users.json", "w") as db:
            json.dump(users_list, db, indent=4)

        return None

    def get_user(self, username: str) -> User | None:
        users_list = self._get_user_list()
        try:
            user = users_list[username]
            return User(**user)
        except KeyError:
            return None

    def _get_user_list(self) -> dict:
        with open("/workdir/src/database/users.json", "r") as file:
            return json.load(file)
