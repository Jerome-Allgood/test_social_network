from rest_framework import serializers

from post.models import Post


class PostSerializer(serializers.ModelSerializer):
	likes = serializers.SerializerMethodField()

	class Meta:
		model = Post
		fields = ('id', 'author', 'body', 'created_at', 'likes')
		read_only_fields = ('id',)

	def get_likes(self, obj):
		return obj.likes.all().count()
