from telegram.ext import Updater,CommandHandler,MessageHandler, Filters

from base import TG_TOKEN, TG_API_URL, do_start, start_test_callback, stop_test_callback
from widgets.echo import do_echo
from widgets.weather import *

import logging


def main():

    updater = Updater(token=TG_TOKEN, base_url=TG_API_URL, use_context=True)
    dispatcher = updater.dispatcher
    jq = updater.job_queue

    menu = {
        "start": do_start,
        "weather": do_weather,
        "test": start_test_callback,
        "stop_test": stop_test_callback,
        "start_weather": start_weather_callback,
        "stop_weather": stop_weather_callback
    }

    for command, handler in menu.items():
        h = CommandHandler(command, handler)
        dispatcher.add_handler(h)

    message_handler = MessageHandler(Filters.text, do_echo)
    dispatcher.add_handler(message_handler)

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
