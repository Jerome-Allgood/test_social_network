from django.urls import path

from register.api.views import CreateUserView, LoginView, LogoutView

urlpatterns = [
    path('users/register/', CreateUserView.as_view()),
    path('users/login/', LoginView.as_view()),
    path('users/logout/', LogoutView.as_view()),

]
