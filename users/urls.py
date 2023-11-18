from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.apps import UsersConfig
from users.views import MyTokenObtainPairView, UserCreateView, UserListView, UserRetrieveView, UserUpdateView, \
    UserDestroyView

app_name = UsersConfig.name

urlpatterns = [
    path('create/', UserCreateView.as_view(), name='create_user'),
    path('', UserListView.as_view(), name='users_list'),
    path('<int:pk>/', UserRetrieveView.as_view(), name='view_user'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='update_user'),
    path('delete/<int:pk>/', UserDestroyView.as_view(), name='delete_user'),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
