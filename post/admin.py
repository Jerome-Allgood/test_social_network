from django.contrib import admin

# Register your models here.
from post.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('id', 'author', 'body', 'created_at', 'updated_at')
	search_fields = ('author', 'body', 'id')
	ordering = ('created_at',)
