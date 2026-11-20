from bot.updater import Updater
from bot.handlers import (
    TextHandler,
    PhotoHandler,
    ContactHandler,
    LocatioinHandler,
    DocumentHandler,
    VoiceHandler,
    VideoHandler,
    DiceHandler,
)

from settings import settings
from calbacks import (
    reply_text,
    reply_photo,
    reply_contact,
    reply_location,
    reply_document,
    reply_voice,
    reply_video,
    reply_dice,
)


def main() -> None:
    updater = Updater(settings.token)

    updater.dispatcher.add_handler(TextHandler(reply_text))
    updater.dispatcher.add_handler(PhotoHandler(reply_photo))
    updater.dispatcher.add_handler(ContactHandler(reply_contact))
    updater.dispatcher.add_handler(LocatioinHandler(reply_location))
    updater.dispatcher.add_handler(DocumentHandler(reply_document))
    updater.dispatcher.add_handler(VoiceHandler(reply_voice))
    updater.dispatcher.add_handler(VideoHandler(reply_video))
    updater.dispatcher.add_handler(DiceHandler(reply_dice))

    updater.start_polling()


if __name__ == "__main__":
    main()
