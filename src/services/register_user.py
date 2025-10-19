from .hash_password import hash_password
from .create_user import create_user
def register_user(user_data: object) -> dict[str, str]:
    password = user_data.password
    hashed_password = hash_password(password)
    new_user = {
        "username": user_data.username,
        "email": user_data.email,
        "password": hashed_password
    }
    create_user(new_user)
    return new_user


