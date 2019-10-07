def do_start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, it's me, " + context.bot.username)


def start_test_callback(update, context):
    jq = context.job_queue
    chat_id = update.effective_chat.id
    job_context = {"txt": "TEST SCHEDULE"}
    job_context.update({"chat_id": chat_id})
    name = str(chat_id) + "_callback_test"
    jq.run_repeating(_callback_minute, interval=60, first=0, context=job_context, name=name)


def _callback_minute(context):
    j = context.job
    chat_id = j.context.get("chat_id")
    context.bot.send_message(chat_id=chat_id, text=j.context.get('txt'))


def stop_test_callback(update, context):
    jq = context.job_queue
    job_name = update.effective_chat.id + "_callback_test"
    jobs = jq.get_jobs_by_name(job_name)
    if len(jobs) != 0:
        for job in jobs:
            job.schedule_removal()
        context.bot.send_message(chat_id=update.effective_chat.id, text="Test successfully stopped! We had " + str(jobs))
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Wooops, we can't stop the test! We have np jobs")

