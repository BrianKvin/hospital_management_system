from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin

from .models import User
from .serializers import RegistrationSerializer, UserSerializer, CustomObtainTokenPairSerializer


# Create your views here.

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomObtainTokenPairSerializer


class RegisterUserView(GenericAPIView, CreateModelMixin):
    serializer_class = RegistrationSerializer
    queryset = User.objects.all()

    def post(self, request):
        return self.create(request)

    # def post(self, request):
    #     user = User.objects.filter(email=request.data['email'])

    #     if user.exists():
    #         return Response({'error': 'Email already registered'}, status=status.HTTP_400_BAD_REQUEST)

    #     serializer = RegistrationSerializer(data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    """Retrieve and updates user details
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)

    # retrieve a single user
    def get(self, request, pk):
        return self.retrieve(request, pk)

    # update details of a single user
    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


class AllUsersView(GenericAPIView, ListModelMixin):
    """Retrieves all users in the database
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return self.list(request)

# class UserView(APIView):
#     """Retrieve and updates user details
#     """
#     permission_classes = (IsAuthenticated,)

#     # retrieve a single user
#     def get(self, request, pk):
#         user = get_object_or_404(User, pk=pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     # update details of a single user
#     def put(self, request, pk):
#         user = get_object_or_404(User, pk=pk)
#         serializer = UserSerializer(user, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class AllUsersView(APIView):
#     """Retrieves all users in the database
#     """
#     permission_classes = (IsAuthenticated,)

#     def get(self, request):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
