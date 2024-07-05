from telegram import Update, constants
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_text(
        f"Здравствуйте, {user.full_name}!\n"
        "Это бот для генерации списка целей игры 'Киллер'.\n"
        "Вам нужно скинуть боту файл с игроками в формате CSV.\n"
        "Формат файла:\n"
        "Имя,Фамилия,Номер комнаты\n"
        "Сделать такой файл можно с помощью электронных таблиц.\n"
        "Скриншоты прилагаются.\n"
    )
    await update.message.reply_photo("assets/tutor-1.png")
    await update.message.reply_photo("assets/tutor-2.png")
    await update.message.reply_document("assets/players.csv", caption="Пример файла")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Вам нужно скинуть боту файл с игроками в формате CSV.\n"
        "Формат файла:\n"
        "Имя,Фамилия,Номер комнаты\n"
        "Сделать такой файл можно с помощью электронных таблиц.\n"
        "Скриншоты прилагаются.\n"
    )
    await update.message.reply_photo("assets/tutor-1.png")
    await update.message.reply_photo("assets/tutor-2.png")
    await update.message.reply_document("assets/players.csv", caption="Пример файла")


async def plaintext(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f"Бот не знает такой команды: '{update.message.text}'"
    )


async def meaningless(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f"Бот не знает такой команды: '{update.message.text}'"
    )
