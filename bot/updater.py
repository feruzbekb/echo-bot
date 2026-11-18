import time

import requests

from bot.bot import Bot
from bot.distpatcher import Dispatcher


class Updater:
    def __init__(self, token: str) -> None:
        self.bot = Bot(token)
        self.dispatcher = Dispatcher(self.bot)

    def start_polling(self) -> None:
        while True:
            for update in self.bot.get_updates():
                self.dispatcher.process_update(update)

                self.bot.last_update_id = update["update_id"] + 1

            time.sleep(0.5)
