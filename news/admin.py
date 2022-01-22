from django.contrib import admin
from news.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "link",
        "creation_date",
        "upvote_count",
        "author_name",
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "post", "author_name", "content", "creation_date"]
