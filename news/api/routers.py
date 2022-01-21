from rest_framework import routers
from news.api.viewsets import PostViewSet, CommentViewSet

router = routers.DefaultRouter()

router.register("post", PostViewSet)
router.register("comment", CommentViewSet)
