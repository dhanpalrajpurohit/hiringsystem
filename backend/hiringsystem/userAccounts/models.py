from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .manager import UserManager

# Create your models here.


class Users(AbstractUser, PermissionsMixin):
    username = None
    email = models.EmailField(_('Email'), unique=True, max_length=200)
    is_Candidate = models.BooleanField(default=True)
    is_Company = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

