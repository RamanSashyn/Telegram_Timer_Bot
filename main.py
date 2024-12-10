import os
from dotenv import load_dotenv
from pytimeparse import parse
import ptbot


def render_progressbar(
    total, iteration, prefix="", suffix="", length=30, fill="█", zfill="░"
):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return "{0} |{1}| {2}% {3}".format(prefix, pbar, percent, suffix)


def notify_progress(secs_left, chat_id, message_id, total_time):
    if secs_left >= 0:
        progress_bar = render_progressbar(total_time, total_time - secs_left)
        message = f"Осталось {secs_left} секунд\n{progress_bar}"
        bot.update_message(chat_id, message_id, message)

    if secs_left == 0:
        bot.create_timer(0.001, choose, chat_id=chat_id)


def choose(chat_id):
    message = "Время вышло!"
    bot.send_message(chat_id, message)


def main(chat_id, question):
    seconds_left = parse(question)

    if seconds_left:
        message = bot.send_message(chat_id, f"Осталось {seconds_left} секунд")
        message_id = message
        bot.create_countdown(
            seconds_left,
            notify_progress,
            chat_id=chat_id,
            message_id=message_id,
            total_time=seconds_left,
        )
    else:
        bot.send_message(
            chat_id,
            "Неверный формат времени. Используйте, например, '5s' или '10m'.",
        )


load_dotenv()
TG_TOKEN = os.getenv("TG_TOKEN")
TG_CHAT_ID = "571873439"


if __name__ == "__main__":
    bot = ptbot.Bot(TG_TOKEN)
    bot.reply_on_message(main)
    bot.run_bot()
