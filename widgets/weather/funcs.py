import requests
from .config import OPEN_WEATHER_API_KEY

def start_test_callback(update, context):
    jq = context.job_queue
    chat_id = update.effective_chat.id
    job_context = {}
    job_context.update({"chat_id": chat_id})
    name = str(chat_id) + "_callback_weather"
    jq.run_repeating(do_weather, interval=60, first=0, context=job_context, name=name)


def do_weather(context):
    j = context.job
    chat_id = j.context.get("chat_id")
    resp = requests.get("https://api.openweathermap.org/data/2.5/forecast?lat=35&lon=139&appid={}".format(OPEN_WEATHER_API_KEY), verify=False)
    context.bot.send_message(chat_id=chat_id, text=resp.status_code)


def stop_weather_callback(update, context):
    jq = context.job_queue
    job_name = str(update.effective_chat.id) + "_callback_weather"
    jobs = jq.get_jobs_by_name(job_name)
    if len(jobs) != 0:
        for job in jobs:
            job.schedule_removal()
        context.bot.send_message(chat_id=update.effective_chat.id, text="Test successfully stopped! We had " + str(jobs))
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Wooops, we can't stop the test! We have np jobs")