from dotenv import load_dotenv
import os

from telegram import Update
from telegram.ext import (
    CommandHandler,
    MessageHandler,
    filters,
    ApplicationBuilder,
)

from handlers.default import *
from handlers.generate import *


def main():
    token = os.environ.get("BOT_TOKEN")
    if token is None:
        print("Error: BOT_TOKEN environment variable not set.")
        return

    app = ApplicationBuilder().token(token).concurrent_updates(False).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.Document.MimeType("text/csv"), generate))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, plaintext))
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    load_dotenv(verbose=True, override=True)
    main()
