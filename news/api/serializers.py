from rest_framework.serializers import ModelSerializer
from news.models import Post, Comment


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'link', 'creation_date', 'upvote_count', 'author_name')


class CommentSerializer(ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'
