from celery import Celery
from flask import current_app as app
from celeryconfig import *
# Initialize Celery
celery = Celery("Blog_Lite_App")
celery.config_from_object("celeryconfig")

# Define the context task for Celery
class ContextTask(celery.Task):
    def __call__(self, *args, **kwargs):
        with app.app_context():
            return self.run(*args, **kwargs)

#Important Commands to be put
#celery -A tasks:celery worker --loglevel=info
#celery -A tasks beat --loglevel=info
#sudo pkill redis-server 
#https://chat.googleapis.com/v1/spaces/AAAA5okRv6s/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=4HBkq8k3YqwSdTYyJ4Ht_WLrk1XRZ5VjiCJGYLEHMoo
#After modification cancel/run celery and then cancel/run app.py . Time is same tho.z