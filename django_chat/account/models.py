from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from django_chat.account.managers import AppUserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_MAX_LENGTH = 20

    username = models.CharField(max_length=USERNAME_MAX_LENGTH, unique=True, null=False, blank=False)
    is_staff = models.BooleanField(default=False)

    objects = AppUserManager()

    USERNAME_FIELD = 'username'
