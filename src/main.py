from fastapi import FastAPI
import requests

app = FastAPI(title="RPG sim")


def get_number(dice:int) -> int:
    response = requests.get(f"https://www.random.org/integers/?num=1&min=1&max={dice}&col=1&base=10&format=plain&rnd=new")
    wynik = int(response.text.strip())
    return wynik

def get_rolls(dice:int, rolls:int) -> list[int]:
    return [get_number(dice) for _ in range(rolls)]

@app.get("/roll")
def response_dice_rolls(dice: int, rolls: int):
    wynik = get_rolls(dice, rolls)
    return{"wynik": wynik}



