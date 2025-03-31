from fastapi import FastAPI, Request
from src.interface.telegram_bot import application
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Super Agent is webhook-ready"}

@app.post("/webhook")
async def telegram_webhook(request: Request):
    json_data = await request.json()
    await application.update_queue.put(json_data)
    return {"ok": True}
