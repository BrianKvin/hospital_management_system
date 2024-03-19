from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token

from .models import User
from hms.models import Patient, Physio


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'phone_number', 'first_name',
                  'last_name', 'is_physio', 'password', 'is_patient']

    def create(self, validated_data):
        phone_number = validated_data.pop('phone_number', '')
        is_physio = validated_data.get('is_physio')
        is_patient = validated_data.get('is_patient')

        if phone_number:
            phone_number = str(phone_number)

        user = User.objects.create_user(
            phone_number=phone_number, **validated_data)

        if is_physio:
            # Create a Physio instance and associate it with the user
            physio, created = Physio.objects.get_or_create(user=user)
            user.is_physio = True
            user.is_staff = True
            user.save()
            return user

        elif is_patient:
            # Create a Patient instance and associate it with the user
            patient, created = Patient.objects.get_or_create(user=user)
            user.is_patient = True
            user.save()
            return user

        return user


class CustomObtainTokenPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user) -> Token:
        token = super().get_token(user)

        if user.is_patient:
            token['role'] = 'patient'
            return token

        elif user.is_physio:
            token['role'] = 'physio'
            return token

        return token


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'phone_number', 'first_name',
                  'last_name', 'is_physio', 'is_patient']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
