from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from post.api.serializers import PostSerializer


class CreatePostView(CreateAPIView):
	permission_classes = [permissions.IsAuthenticated,]
	serializer_class = PostSerializer
