from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title of news post")
    link = models.URLField(max_length=255, verbose_name="Link of news post")
    creation_date = models.DateTimeField(auto_now_add=True)
    upvote_count = models.IntegerField(default=0)
    author_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.title}-{self.author_name}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.post.title}-{self.content}"