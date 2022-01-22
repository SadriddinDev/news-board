import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NewsAPI.settings")

app = Celery("NewsAPI")

app.config_from_object("django.conf:settings", namespace="CELERY")


app.autodiscover_tasks()


app.conf.beat_schedule = {
    "run-me-every-ten-seconds": {
        "task": "news.tasks.reset_upvote_count",
        "schedule": crontab(minute=0, hour=0),
    }
}
