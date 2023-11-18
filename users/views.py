from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.serializers import UserSerializer, MyTokenObtainPairSerializer


class UserCreateView(generics.CreateAPIView):
    """ Представление регистрации пользователя """

    serializer_class = UserSerializer


class UserListView(generics.ListAPIView):
    """ Список пользователей """

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveView(generics.RetrieveAPIView):
    """ Просмотр профиля пользователя """

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateView(generics.UpdateAPIView):
    """ Редактирование профиля пользователя """

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyView(generics.DestroyAPIView):
    """ Удаление пользователя """

    queryset = User.objects.all()


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
