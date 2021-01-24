from django.urls import path

from post.api.views import CreatePostView, ListPostView

urlpatterns = [
    path('post/create/', CreatePostView.as_view()),
    path('post/list/', ListPostView.as_view()),

]