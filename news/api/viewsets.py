from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from news.models import Post, Comment
from news.api.serializers import PostSerializer, CommentSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=["get"])
    def upvote_post(self, request, pk=None):
        try:
            post = Post.objects.get(id=pk)
            post.upvote_count += 1
            post.save()
            return Response(PostSerializer(post, many=False).data)
        except Post.DoesNotExist:
            return Response(
                {"message": f"{pk} post object does not exist!"},
                status=status.HTTP_404_NOT_FOUND,
            )


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
