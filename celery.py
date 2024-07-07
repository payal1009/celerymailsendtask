
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab #crontabl for scheduling task at perticular time


'''
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryproject.settings')

app = Celery('celeryproject')
#app.conf.enable_utc=False
#app.conf.update(timezone='Asia/Kolkata')
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()
# celery_app.py
'''


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryproject.settings')
app = Celery('celeryproject')
app.config_from_object(settings, namespace="CELERY")

app.conf.update(
    broker_url='redis://127.0.0.1:6379',
    result_backend='redis://127.0.0.1:6379',
    broker_connection_retry_on_startup=True,
    task_serializer='json',
    result_serializer='json',
    accept_content=['json'],
    #timezone='UTC',
    timezone='Asia/Kolkata'
    #enable_utc=True
)


app.conf.beat_schedule = {  
    'send-mail-every-day-at-8':  {
        'task': 'send_mail.task.test_mail',
        'schedule': crontab(minute='*'), #it will send mail every minute
    }  
      
}  


app.autodiscover_tasks()
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')