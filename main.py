from telegram import Bot
from telegram.ext import Updater,CommandHandler,MessageHandler, Filters
from echo.config import TG_TOKEN
from echo.config import TG_API_URL
from echo.config import OPEN_WEATHER_API_KEY

import requests


def do_start(bot: Bot, update: Updater):
    bot.send_message(chat_id=update.message.chat_id, text="Hello world")


def do_weather(bot: Bot, update: Updater):
    # resp = requests.get("api.openweathermap.org/data/2.5/forecast?lat=35&lon=139&appid={}".format(OPEN_WEATHER_API_KEY))
    bot.send_message(chat_id=update.message.chat_id, text="Requesting data ...")
    resp = requests.get("https://postman-echo.com/get?foo1=bar1&foo2=bar2")
    bot.send_message(chat_id=update.message.chat_id, text=resp.text)


def do_echo(bot: Bot, update: Updater):
    text = update.message.text
    chat_id = update.message.chat_id

    if text == "погода":
        resp = requests.get("api.openweathermap.org/data/2.5/forecast?lat=35&lon=139&appid={}".format(OPEN_WEATHER_API_KEY))
        print(resp.status_code)
        print(resp.text)
        text = resp.text
    bot.send_message(chat_id=update.message.chat_id, text="Ваш ID: {}\n{}".format(chat_id, text))


def main():

    bot = Bot(TG_TOKEN,base_url=TG_API_URL)

    updater = Updater(bot=bot)

    menu = {
        "start": do_start,
        "weather": do_weather
    }

    for command, handler in menu.items():
        h = CommandHandler(command, handler)
        updater.dispatcher.add_handler(h)

    message_handler = MessageHandler(Filters.text, do_echo)
    updater.dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()