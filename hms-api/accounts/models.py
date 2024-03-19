from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import RegexValidator
from django.utils import timezone

phone_validator = RegexValidator(
    r"^(\+?\d{0,4})?\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{4}\)?)?$", "The phone number provided is invalid")


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, phone_number, first_name=None, last_name=None, password=None, is_physio=False, is_patient=False):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError('Email must be set')
        if not phone_number:
            raise ValueError('Phone number must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, first_name=first_name,
                          last_name=last_name, is_physio=is_physio, is_patient=is_patient)
        user.set_password(password)
        user.save()
        return user

    def create_patient(self, email, phone_number, first_name=None, last_name=None, password=None, is_physio=False, is_patient=False):
        """
        Create and save a user with is_patient status
        """
        user = self.create_user(email=email, phone_number=phone_number, first_name=first_name, password=password,
                                last_name=last_name, is_physio=is_physio, is_patient=is_patient)
        user.is_patient = True
        user.save()
        return user

    def create_physio(self, email, phone_number, first_name=None, last_name=None, password=None, is_physio=False, is_patient=False):
        """
        Create and save a user with is_doctor, is_staff, is_admin status
        """
        user = self.create_user(email=email, phone_number=phone_number, first_name=first_name, password=password,
                                last_name=last_name, is_physio=is_physio, is_patient=is_patient)
        user.is_physio = True
        user.is_staff = True
        user.save()
        return user

    def create_superuser(self, email, phone_number, password):
        """
        Create and save a user with is_superuser status
        """
        user = self.create_user(phone_number=phone_number,
                                email=email, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(
        max_length=16, validators=[phone_validator])
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_physio = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    objects = UserManager()

    def __str__(self) -> str:
        return self.email
