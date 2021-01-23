from django.db import models

# Create your models here.
from register.models import User


class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
	body = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True, null=True)
	updated_at = models.DateTimeField(auto_now=True, null=True)

	def __str__(self):
		return f'Post id {self.id} by {self.author}'
