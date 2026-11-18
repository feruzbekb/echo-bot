from bot.context import Context
from bot.handlers import BaseHandler


class Dispatcher:
    def __init__(self, bot) -> None:
        self.context = Context(bot)
        self.handlers: list[BaseHandler] = []

    def add_handler(self, handler):
        if handler not in self.handlers:
            self.handlers.append(handler)

    def process_update(self, update: dict) -> None:
        for handler in self.handlers:
            if handler.check_update(update):
                handler.handle_update(update, self.context)
                break
