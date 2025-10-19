from pydantic import BaseModel, EmailStr, field_validator, Field
from json import load

class RegisterData(BaseModel):  # We need a model that will represent data that user will be sending during account creation process.
    username: str = Field(min_length=3)
    email: EmailStr
    password: str

    @field_validator("password", mode="after")
    def validate_password(cls, password: str, username: str) -> str:
        numbers = 0
        special_char = 0
        upper_case = 0
        if len(password) < 8:
            raise ValueError("Password must be atleast 8 characters long")
        if password == username:
            raise ValueError("Password can't be the same as username")
        if password.isalpha():
            raise ValueError(
                "Password must have atleast 2 numbers and one special character and one upper case letter"
            )
        for letter in password:
            if letter.isspace():
                raise ValueError("Password can't have spaces")
            if letter.isnumeric():
                numbers += 1
            if (
                33 <= ord(letter) <= 47
                or 58 <= ord(letter) <= 64
                or 91 <= ord(letter) <= 96
                or 123 <= ord(letter) <= 126
            ):
                special_char += 1
            if letter.isupper():
                upper_case += 1
        if numbers < 2:
            raise ValueError(
                "Password must have atleast 2 numbers and one special character"
            )
        if special_char < 1:
            raise ValueError("Password must have atleast 1 special character")
        if upper_case < 1:
            raise ValueError("Password must have atleast one upper case letter")
        return password
    
    @field_validator("username", mode="after")
    def validate_username(cls, username:str) -> str:
        with open("/workdir/src/database/users.json", "r") as file:
            users_list = load(file)
            if username in users_list["usernames"]:
                raise ValueError("Username already taken")
        return username