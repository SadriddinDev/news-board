from NewsAPI.celery import app
from news.models import Post


@app.task
def reset_upvote_count():
    Post.objects.all().update(upvote_count=0)
    print("Reset all Post upvote count")
