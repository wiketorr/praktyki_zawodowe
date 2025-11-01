from pydantic import BaseModel, field_validator, Field

class CreateSessionData(BaseModel):
    name: str = Field(min_length=4)
    password: str
    player_cap: int = 4
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
    @field_validator("player_cap", mode="after")
    def validate_player_cap(cls,player_cap:int) -> int:
        if player_cap > 20:
            raise ValueError("Session can take up to 20 players")
        elif player_cap < 1:
            raise ValueError("Session need atleast 1 player")
        else:
            return player_cap