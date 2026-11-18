from bot.context import Context


def reply_text(update: dict, context: Context):
    context.bot.send_message(update["message"]["chat"]["id"], update["message"]["text"])


def reply_photo(update: dict, context: Context):
    context.bot.send_photo(update["message"]["chat"]["id"], update["message"]["photo"])


def reply_contact(update: dict, context: Context):
    print("contact keldi")


def reply_location(update: dict, context: Context):
    print("lcoation keldi")
