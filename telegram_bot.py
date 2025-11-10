import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, CommandHandler, filters

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

APPLE_PATH = os.path.join(os.path.dirname(__file__), "images", "apple.jpg")
CARROT_PATH = os.path.join(os.path.dirname(__file__), "images", "carrot.jpg")
BOOK_PATH = os.path.join(os.path.dirname(__file__), "images", "book.jpg")
LEMON_PATH = os.path.join(os.path.dirname(__file__), "images", "lemons.jpg")
CAT_PATH = os.path.join(os.path.dirname(__file__), "images", "cat.jpg")
HOT_PATH = os.path.join(os.path.dirname(__file__), "images", "hotwheels.jpg")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send 'apple' or 'carrot' to receive a picture.")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (update.message.text or "").strip().lower()
    if text == "apple":
        if os.path.exists(APPLE_PATH):
            await update.message.reply_photo(photo=open(APPLE_PATH, "rb"))
        else:
            await update.message.reply_text("Apple image not found on server.")
    elif text == "carrot":
        if os.path.exists(CARROT_PATH):
            await update.message.reply_photo(photo=open(CARROT_PATH, "rb"))
        else:
            await update.message.reply_text("Carrot image not found on server.")
    elif text == "book":
        if os.path.exists(BOOK_PATH):
            await update.message.reply_photo(photo=open(BOOK_PATH, "rb"))
        else:
            await update.message.reply_text("Carrot image not found on server.")
    elif text == "lemon":
        if os.path.exists(CARROT_PATH):
            await update.message.reply_photo(photo=open(LEMON_PATH, "rb"))
        else:
            await update.message.reply_text("Carrot image not found on server.")

    elif text == "cat":
        if os.path.exists(CARROT_PATH):
            await update.message.reply_photo(photo=open(CAT_PATH, "rb"))
    elif text == "hot wheels":
        if os.path.exists(CARROT_PATH):
            await update.message.reply_photo(photo=open(HOT_PATH, "rb"))

    else:
        await update.message.reply_text("I don't know yet this object. Send 'apple', 'carrot', 'lemon', 'book', 'cat' or 'hot wheels'.")

def main():
    token = ''
    #token = os.getenv("")
    if not token:
        logger.error("TELEGRAM_TOKEN environment variable is not set.")
        return

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.run_polling()

if __name__ == "__main__":
    main()