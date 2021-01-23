from django.urls import path

from post.api.views import CreatePostView

urlpatterns = [
    path('post/create/', CreatePostView.as_view()),
]
