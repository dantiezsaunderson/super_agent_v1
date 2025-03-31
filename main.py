from fastapi import FastAPI
from src.interface.telegram_bot import run_bot
import asyncio
import os

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    token = os.getenv("TELEGRAM_BOT_TOKEN", "")
    if token:
        asyncio.create_task(run_bot(token))
    else:
        print("TELEGRAM_BOT_TOKEN is missing!")

@app.get("/")
def read_root():
    return {"status": "Super Agent is running"}
