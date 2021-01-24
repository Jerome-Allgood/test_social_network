from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView

from post.api.serializers import PostSerializer
from post.models import Post


class CreatePostView(CreateAPIView):
	permission_classes = [permissions.IsAuthenticated,]
	serializer_class = PostSerializer


class ListPostView(ListAPIView):
	permission_classes = [permissions.IsAuthenticated,]
	serializer_class = PostSerializer
	queryset = Post.objects.all()
