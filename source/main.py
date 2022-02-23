from readline import set_completion_display_matches_hook
from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv
from os import environ as ose
import time

load_dotenv()
BOT_TOKEN = ose.get("BOT_TOKEN")
print(BOT_TOKEN)


def hola(update, context):
    print(update)
    print(context)
    while True:
        time.sleep(5)
        context.bot.send_message(update.effective_chat.id, text="chau")


def run():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    updater.dispatcher.add_handler(CommandHandler("hola", hola))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    run()
