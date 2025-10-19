import hashlib


def hash_password(password: str) -> str:
    hash = hashlib.new("SHA384")
    hash.update(password.encode())
    return hash.hexdigest()

hash_password("hasło123!")