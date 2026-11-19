from bot.context import Context


class BaseHandler:
    def __init__(self, callback):
        self.callback = callback

    def handle_update(self, update: dict, context: Context) -> None:
        self.callback(update, context)


class TextHandler(BaseHandler):
    def check_update(self, update: dict) -> bool:
        message = update.get("message", {})
        text = message.get("text")

        if text:
            return True
        else:
            return False


class PhotoHandler(BaseHandler):
    def check_update(self, update: dict) -> bool:
        message = update.get("message", {})
        photo = message.get("photo")

        if photo:
            return True
        else:
            return False


class LocatioinHandler(BaseHandler):
    def check_update(self, update: dict) -> bool:
        message = update.get("message", {})
        location = message.get("location")

        if location:
            return True
        else:
            return False


class ContactHandler(BaseHandler):
    def check_update(self, update: dict) -> bool:
        message = update.get("message", {})
        contact = message.get("contact")

        if contact:
            return True
        else:
            return False


class DocumentHandler(BaseHandler):
    def check_update(self, update: dict) -> bool:
        message = update.get("message", {})
        document = message.get("document")

        if document:
            return True
        else:
            return False


class VoiceHandler(BaseHandler):
    def check_update(self, update: dict) -> bool:
        message = update.get("message", {})
        voice = message.get("voice")

        if voice:
            return True
        else:
            return False


class VideoHandler(BaseHandler):
    def check_update(self, update: dict) -> bool:
        message = update.get("message", {})
        video = message.get("video")

        if video:
            return True
        else:
            return False


class DiceHandler(BaseHandler):
    def check_update(self, update: dict) -> bool:
        message = update.get("message", {})
        dice = message.get("dice")

        if dice:
            return True
        else:
            return False
