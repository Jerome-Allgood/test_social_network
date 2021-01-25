from django.urls import path

from register.api.views import CreateUserView, LoginView, LogoutView

urlpatterns = [
    path('users/register/', CreateUserView.as_view(), name='register'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/logout/', LogoutView.as_view(), name='logout'),

]
