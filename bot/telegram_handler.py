from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

from config.config_loader import Config
from core.task_handler import TaskHandler

def authorized(user_id):
    return user_id == Config.TELEGRAM_USER_ID

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not authorized(update.effective_user.id):
        return
    await update.message.reply_text("🚀 AI Coding Assistant Ready")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not authorized(update.effective_user.id):
        return
    await update.message.reply_text("/newproject - Start new project\n/status")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not authorized(update.effective_user.id):
        return

    await update.message.reply_text("⚙️ Processing...")

    result = TaskHandler.handle_prompt(update.message.text)

    response = f"""
✅ Project Created: {result['project']}

📂 Path: {result['path']}
🌐 Repo: {result['repo']}

🧠 Summary:
{result['summary']}
"""
    await update.message.reply_text(response)

def run_bot():
    app = ApplicationBuilder().token(Config.TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()
