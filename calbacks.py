from bot.context import Context


def reply_text(update: dict, context: Context):
    context.bot.send_message(update["message"]["chat"]["id"], update["message"]["text"])


def reply_photo(update: dict, context: Context):
    context.bot.send_photo(update["message"]["chat"]["id"], update["message"]["photo"])


def reply_contact(update: dict, context: Context):
    context.bot.send_contact(
        update["message"]["chat"]["id"],
        update["message"]["contact"]["phone_number"],
        update["message"]["contact"]["first_name"],
    )


def reply_location(update: dict, context: Context):
    context.bot.send_location(
        update["message"]["chat"]["id"],
        update["message"]["location"]["latitude"],
        update["message"]["location"]["longitude"],
    )


def reply_document(update: dict, context: Context):
    context.bot.send_document(
        update["message"]["chat"]["id"], update["message"]["document"]["file_id"]
    )


def reply_voice(update: dict, context: Context):
    context.bot.send_voice(
        update["message"]["chat"]["id"], update["message"]["voice"]["file_id"]
    )


def reply_video(update: dict, context: Context):
    context.bot.send_video(
        update["message"]["chat"]["id"], update["message"]["video"]["file_id"]
    )


def reply_dice(update: dict, context: Context):
    context.bot.send_dice(
        update["message"]["chat"]["id"], update["message"]["dice"]["emoji"]
    )
