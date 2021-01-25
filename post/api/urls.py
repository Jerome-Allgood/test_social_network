from django.urls import path

from post.api.views import CreatePostView, ListPostView, LikePostView

urlpatterns = [
    path('post/create/', CreatePostView.as_view(), name='create_post'),
    path('post/list/', ListPostView.as_view(), name='list_post'),
    path('post/<int:pk>/like/', LikePostView.as_view(), name='like_post'),

]
