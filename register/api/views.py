from django.contrib.auth import authenticate, login, logout

from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView

from register.api.serializers import UserSerializer, UserLoginSerializer


class CreateUserView(CreateAPIView):
    """Creates new user.
    """

    permission_classes = [permissions.AllowAny,]
    serializer_class = UserSerializer


def get_tokens_for_user(user):
    """Returns generated pair of JWT tokens for user.
    """
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class LoginView(APIView):
    """
    Returns tokens for JWT authentication.

    Token **access** should added to headers as Authorization Bearer.
    Token **refresh** can be used for renewing access token [here][ref]

    [ref]: http://localhost:8000/token/refresh/
    """

    serializer_class = UserLoginSerializer

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            data = get_tokens_for_user(user)
            return Response(status=status.HTTP_200_OK, data=data)
        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data={'status': 'failed'})


class LogoutView(APIView):
    """Logout user from system.
    """

    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
