import ptbot

from dotenv import load_dotenv
import os

import random

load_dotenv()

tg_token = os.getenv("TG_TOKEN")
TG_CHAT_ID = "571873439"
bot = ptbot.Bot(tg_token)

def wait(chat_id, question):
    bot.create_timer(5, choose, chat_id=chat_id, question=question)

def choose(chat_id, question):
    message = "Время вышло!".format(question)
    bot.send_message(chat_id, message)
    print("Мне написал пользователь с ID:", chat_id)
    print("Он спрашивал:", question)
    print("Я ответил:", message)

bot = ptbot.Bot(tg_token)
bot.reply_on_message(wait)
bot.run_bot()
