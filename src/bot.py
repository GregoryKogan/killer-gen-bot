from dotenv import load_dotenv
import os

from telegram import Update
from telegram.ext import (
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
    ApplicationBuilder,
)

from handlers.default import *
from handlers.generate import *


def main():
    app = (
        ApplicationBuilder()
        .token(os.environ.get("BOT_TOKEN"))
        .concurrent_updates(False)
        .build()
    )
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, plaintext))
    app.add_handler(MessageHandler(filters.TEXT, meaningless))
    app.add_handler(MessageHandler(filters.Document.TEXT, generate))

    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    load_dotenv(verbose=True, override=True)
    main()
