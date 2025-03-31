import asyncio
from src.interface.telegram_bot import run_bot
import os

if __name__ == "__main__":
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if token:
        asyncio.run(run_bot(token))
    else:
        print("TELEGRAM_BOT_TOKEN is missing!")
