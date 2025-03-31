from fastapi import FastAPI, Request
from src.interface.telegram_bot import application

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Superagent101 API is running"}

@app.post("/webhook")
async def telegram_webhook(request: Request):
    json_data = await request.json()
    await application.update_queue.put(json_data)
    return {"ok": True}
