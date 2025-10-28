from pwdlib import PasswordHash

def hash_password( password: str) -> str:
        hash = PasswordHash.recommended()
        return hash.hash(password)