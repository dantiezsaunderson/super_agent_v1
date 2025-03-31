import os
import asyncio
from src.interface.telegram_bot import application

async def run_bot():
    await application.initialize()
    await application.start()
    print("Bot running via polling")

if __name__ == "__main__":
    asyncio.run(run_bot())
