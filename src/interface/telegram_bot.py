import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Initialize bot
application = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()

# Handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, I'm Superagent101! Type /help to see what I can do.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("/start - Start the bot\n/help - Show available commands\n/code - Generate Python code")

async def code_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Here's a sample Python snippet:\n\nprint('Hello from Superagent101')")

# Register handlers
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help_command))
application.add_handler(CommandHandler("code", code_command))

# Webhook runner
async def run_bot():
    await application.initialize()
    await application.start()
    print("Telegram bot is now live via webhook.")
