from django.urls import path
from .views import RegisterUserView, UserView, AllUsersView, CustomTokenObtainPairView
from rest_framework_simplejwt.views import (TokenRefreshView,)


urlpatterns = [
    path('users/', AllUsersView.as_view()),
    path('users/<int:pk>/', UserView.as_view()),
    path('register/', RegisterUserView.as_view()),
    path('login/', CustomTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
