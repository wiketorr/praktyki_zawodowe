from src.database.user_repository import UserRepository
from src.api.models.user_data import RegisterData
from src.app.models.app_models import User
from src.app.models.app_models import Token
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import HTTPException, status


import jwt
from pwdlib import PasswordHash
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta, timezone


class UserService:
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    def __init__(self, user_repository: UserRepository, secret_key: str):
        self._user_repository = user_repository
        self._secret_key = secret_key

    def register_user(self, user_data: RegisterData) -> User:
        if self._user_repository.get_user(user_data.username):
            raise ValueError("Username already taken")
        password = user_data.password
        hashed_password = self._hash_password(password)
        new_user = User(
            **{
                "username": user_data.username,
                "email": user_data.email,
                "password": hashed_password,
            }
        )
        self._user_repository.save_user(new_user)
        return new_user

    def _create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwd = jwt.encode(to_encode, self._secret_key, algorithm=self.ALGORITHM)
        return encoded_jwd

    def login_for_access_token(self, form_data: OAuth2PasswordRequestForm) -> Token:
        user = self._authenticate_user(form_data.username, form_data.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid password or username",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = self._create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )
        return Token(access_token=access_token, token_type="Bearer")

    def _authenticate_user(self, username, password):
        user = self._user_repository.get_user(username)
        if not user:
            return False
        if not self._verify_password(password, user.password):
            return False
        return user

    def get_current_user(self, token: str):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, self._secret_key, algorithms=[self.ALGORITHM])
            username = payload.get("sub")
            if username is None:
                raise credentials_exception
        except InvalidTokenError:
            raise credentials_exception
        user = self._user_repository.get_user(username)
        if user is None:
            raise credentials_exception
        return user

    def _verify_password(self, plain_password, hashed_password):
        hash = PasswordHash.recommended()
        return hash.verify(plain_password, hashed_password)

    def _hash_password(self, password: str) -> str:
        hash = PasswordHash.recommended()
        return hash.hash(password)
