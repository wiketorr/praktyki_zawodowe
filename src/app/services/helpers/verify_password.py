from pwdlib import PasswordHash

def verify_password(plain_password, hashed_password):
    hash = PasswordHash.recommended()
    return hash.verify(plain_password, hashed_password)