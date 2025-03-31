from fastapi import FastAPI, Request
from src.interface.telegram_bot import application

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Superagent101 is live"}

@app.post("/webhook")
async def telegram_webhook(request: Request):
    update = await request.json()
    await application.update_queue.put(update)
    return {"ok": True}
