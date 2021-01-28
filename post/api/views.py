from django.shortcuts import get_object_or_404

from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.response import Response

from post.api.serializers import PostSerializer
from post.models import Post


class CreatePostView(CreateAPIView):
	"""Creates new Post.

	Required parameters
	-----------
	body: 'text'
	"""

	permission_classes = [permissions.IsAuthenticated,]
	serializer_class = PostSerializer

	def create(self, request, *args, **kwargs):
		body = request.data.get('body')
		author = request.user.id
		serializer = self.get_serializer(data={
			'body': body,
			'author': author,
		})
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED,
						headers=headers)


class ListPostView(ListAPIView):
	"""Returns a list of all posts in the system."""

	permission_classes = [permissions.IsAuthenticated,]
	serializer_class = PostSerializer
	queryset = Post.objects.all()


class LikePostView(UpdateAPIView):
	"""Creates or removes relation between User and Post.
	"""

	permission_classes = [permissions.IsAuthenticated,]

	def post(self, request, pk):
		post = get_object_or_404(Post, id=pk)
		user = request.user

		if post in user.liked_posts.all():
			user.liked_posts.remove(post)
			message = f'Post {post.id} is unliked by user {user.id}'
		else:
			user.liked_posts.add(post)
			message = f'Post {post.id} is liked by user {user.id}'
		return Response(status=status.HTTP_200_OK,
						data={'message': message})
