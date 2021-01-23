from django.urls import path

from register.api.views import CreateUserView

urlpatterns = [
    path('users/register/', CreateUserView.as_view()),
]
