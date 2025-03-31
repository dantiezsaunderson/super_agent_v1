from fastapi import FastAPI
from src.interface.telegram_bot import run_bot

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    import os
    token = os.getenv("TELEGRAM_BOT_TOKEN", "")
    if token:
        run_bot(token)
    else:
        print("TELEGRAM_BOT_TOKEN is missing!")

@app.get("/")
def read_root():
    return {"status": "Super Agent is running"}
