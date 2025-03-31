import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from .ai_service import ai_service

application = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()

# Handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! I'm Superagent101. Type /help to see what I can do.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Activate the bot\n/help - Show this list\n/code - Generate code with AI\n/image - Generate images with AI\n/research - Research a topic with AI"
    )

async def code_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get the prompt from the message text
    message_text = update.message.text
    prompt = message_text.replace("/code", "").strip()
    
    if not prompt:
        await update.message.reply_text("Please provide a description of the code you want. Example: /code a Python function to calculate fibonacci numbers")
        return
    
    await update.message.reply_text("Generating code, please wait...")
    code_result = ai_service.generate_code(prompt)
    await update.message.reply_text(f"Here's your generated code:\n\n{code_result}")

async def image_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get the prompt from the message text
    message_text = update.message.text
    prompt = message_text.replace("/image", "").strip()
    
    if not prompt:
        await update.message.reply_text("Please provide a description of the image you want. Example: /image a cat wearing a space suit")
        return
    
    await update.message.reply_text("Generating image, please wait...")
    image_url = ai_service.generate_image(prompt)
    
    if image_url and not image_url.startswith("Error"):
        await update.message.reply_photo(image_url, caption=f"Generated image for: {prompt}")
    else:
        await update.message.reply_text(image_url)  # This will be the error message

async def research_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get the query from the message text
    message_text = update.message.text
    query = message_text.replace("/research", "").strip()
    
    if not query:
        await update.message.reply_text("Please provide a topic to research. Example: /research quantum computing")
        return
    
    await update.message.reply_text("Researching your topic, please wait...")
    research_result = ai_service.research(query)
    await update.message.reply_text(f"Research on '{query}':\n\n{research_result}")

# Register handlers
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help_command))
application.add_handler(CommandHandler("code", code_command))
application.add_handler(CommandHandler("image", image_command))
application.add_handler(CommandHandler("research", research_command))
