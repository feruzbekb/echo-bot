from bot.updater import Updater
from bot.handlers import TextHandler, PhotoHandler, ContactHandler, LocatioinHandler

from settings import settings
from calbacks import reply_text, reply_photo, reply_contact, reply_location


def main() -> None:
    updater = Updater(settings.token)

    updater.dispatcher.add_handler(TextHandler(reply_text))
    updater.dispatcher.add_handler(PhotoHandler(reply_photo))
    updater.dispatcher.add_handler(ContactHandler(reply_contact))
    updater.dispatcher.add_handler(LocatioinHandler(reply_location))

    updater.start_polling()


if __name__ == "__main__":
    main()
