import ptbot
from dotenv import load_dotenv
import os
from pytimeparse import parse

load_dotenv()

tg_token = os.getenv("TG_TOKEN")
TG_CHAT_ID = "571873439"
bot = ptbot.Bot(tg_token)

last_message_text = None


def notify_progress(secs_left, chat_id, message_id):
    global last_message_text

    if secs_left > 0:
        message = f"Осталось {secs_left} секунд"
    else:
        message = "Осталось 0 секунд"

    if message != last_message_text:
        bot.update_message(chat_id, message_id, message)
        last_message_text = message

    if secs_left == 0:
        bot.create_timer(0.001, choose, chat_id=chat_id)


def choose(chat_id):
    message = "Время вышло!"
    bot.send_message(chat_id, message)


def wait(chat_id, question):
    global last_message_text

    seconds_left = parse(question)

    if seconds_left:
        message = f"Осталось {seconds_left} секунд"
        message_id = bot.send_message(chat_id, message)
        last_message_text = message
        bot.create_countdown(seconds_left, notify_progress, chat_id=chat_id, message_id=message_id)
    else:
        bot.send_message(chat_id, "Неверный формат времени. Используйте, например, '5s' или '10m'.")

bot = ptbot.Bot(tg_token)
bot.reply_on_message(wait)
bot.run_bot()
