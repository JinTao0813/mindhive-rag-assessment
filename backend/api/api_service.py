from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/drinkware")
def get_drinkware():
    with open("../scraper/data/drinkware.json", "r", encoding="utf-8") as f:
        return json.load(f)