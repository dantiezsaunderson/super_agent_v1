from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

application = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, I'm Superagent101!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("/start - Start the bot\n/help - List commands\n/code - Generate code")

async def code_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Here's some sample Python code:\n\nprint('Hello from Superagent101')")

application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help_command))
application.add_handler(CommandHandler("code", code_command))

async def run_bot():
    await application.initialize()
    await application.start()
    print("Bot is webhook-ready and running.")
