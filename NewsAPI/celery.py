import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsAPI.settings')
app = Celery('NewsAPI')
app.config_from_object('django.conf:settings', namespace='CELERY')

@app.task
def add(x, y):
    z = x + y
    print(z)

app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'add',
        'schedule': 30.0,
        'args': (16, 16)
    },
}
app.conf.timezone = 'UTC'


app.autodiscover_tasks()