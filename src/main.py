from fastapi import FastAPI
import requests
import secrets

app = FastAPI(title="RPG sim")


def get_number(dice: int) -> int:
    response = requests.get(
        f"https://www.random.org/integers/?num=1&min=1&max={dice}&col=1&base=10&format=plain&rnd=new"
    )
    result = int(response.text.strip())
    return result


def get_rolls(dice: int, rolls: int) -> list[int]:
    return [get_number(dice) for _ in range(rolls)]


@app.get("/roll")
def response_dice_rolls(dice: int, rolls: int) -> dict[str, list[int]]:
    result = get_rolls(dice, rolls)
    return {"result": result}


def roll_dice(dice: int) -> int:
    return secrets.randbelow(dice) + 1


def get_rolls_secrets(dice: int, rolls: int) -> list[int]:
    return [roll_dice(dice) for _ in range(rolls)]


@app.get("/secret_roll")
def response_secret(dice: int, rolls: int) -> dict[str, list[int]]:
    result = get_rolls_secrets(dice, rolls)
    return {"result": result}
