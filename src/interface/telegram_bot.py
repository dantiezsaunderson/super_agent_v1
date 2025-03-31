import logging
from telegram import Update
from telegram.ext import ContextTypes, Application, CommandHandler, MessageHandler, filters

class TelegramInterface:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Hello! I’m your AI super-agent. Type a command to get started.")

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        help_text = (
            "/start - Start the bot\n"
            "/help - Show this help message\n"
            "/code - Generate or run code\n"
            "/image - Generate an image\n"
            "/research - Do web research"
        )
        await update.message.reply_text(help_text)

    async def code_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        prompt = " ".join(context.args) if context.args else "Write a Python script to print Hello World"
        # Dummy response for now; replace with real agent logic
        code = f"print('Hello from your code agent! Prompt was: {prompt}')"
        await update.message.reply_text(f"Here’s your generated code:

{code}")

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        message_text = update.message.text.lower()

        if "code" in message_text or "script" in message_text:
            context.args = [message_text]
            await self.code_command(update, context)
        else:
            await update.message.reply_text("Sorry, I didn’t understand. Try typing /help for available commands.")

def run_bot(token: str):
    app = Application.builder().token(token).build()
    interface = TelegramInterface()

    app.add_handler(CommandHandler("start", interface.start))
    app.add_handler(CommandHandler("help", interface.help_command))
    app.add_handler(CommandHandler("code", interface.code_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, interface.handle_message))

    print("Bot is running...")
    app.run_polling()
