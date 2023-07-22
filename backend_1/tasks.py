from workers import celery
from flask import current_app as app
from celery import Celery
from celery.schedules import crontab
from httplib2 import Http
from json import dumps
from datetime import datetime, time

celery = Celery(__name__)
celery.conf.broker_url = 'redis://localhost:6379/0'
celery.conf.result_backend = 'redis://localhost:6379/1'

@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(24 * 60 * 60, send_daily_reminder.s())

@celery.task
def send_daily_reminder():
    current_time = datetime.now().time()
    if current_time.hour == 12 and current_time.minute == 52:
        chat_space_url = 'https://chat.googleapis.com/v1/spaces/AAAA5okRv6s/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=4HBkq8k3YqwSdTYyJ4Ht_WLrk1XRZ5VjiCJGYLEHMoo'
        message = "Hello User, this is your daily reminder.Please book your tickets and check out new offers"
        send_message_to_chat_space(chat_space_url, message)

def send_message_to_chat_space(chat_space_url, message):
    http_obj = Http()
    payload = {'text': message}
    payload_json = dumps(payload)
    response, content = http_obj.request(chat_space_url, method='POST', body=payload_json)
    if response.status == 200:
        app.logger.info("Message sent successfully to Google Chat space.")
    else:
        app.logger.error("Failed to send message to Google Chat space.")
