from telegram import Update, constants
from telegram.ext import ContextTypes
import os
import random


class Player:
    def __init__(self, name, last_name, room):
        self.name = name
        self.last_name = last_name
        self.room = room


def gen_targets(players):
    is_ok = False
    while not is_ok:
        random.shuffle(players)
        is_ok = all(
            players[i].room != players[(i + 1) % len(players)].room
            for i in range(len(players))
        )
    return players


async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file = await context.bot.get_file(update.message.document)
    await file.download_to_drive("players.csv")
    players = []
    with open("players.csv", "r") as file:
        for line in file:
            name, last_name, room = list(
                map(lambda x: x.strip(), line.strip().split(","))
            )
            players.append(Player(name, last_name, room))
    os.remove("players.csv")

    players = gen_targets(players)

    msg = "Список целей:\n"
    for i in range(len(players)):
        msg += f"{players[i].name} {players[i].last_name} -> {players[(i + 1) % len(players)].name} {players[(i + 1) % len(players)].last_name}\n"

    await update.message.reply_text(msg)
