def starter(start_func):
    def wrapper(update, context):
        chat_id = update.effective_chat.id
        j_context = {"chat_id": chat_id}
        name = str(chat_id) + "_callback_weather"
        start_func(context, j_context, name)

    return wrapper

# TODO попробовать реализовать декораторы для старта и остановки тасков по расписанию + добавить добавление/проверку/удаление по базе