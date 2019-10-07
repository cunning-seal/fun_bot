def do_echo(update, context):
    text = update.message.text
    chat_id = update.effective_chat.id

    context.bot.send_message(chat_id=chat_id, text="Ваш ID: {}\n{}".format(chat_id, text))