from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from uuid import uuid4


class MyUser(AbstractUser, PermissionsMixin):
    id = models.UUIDField(default=uuid4, primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64, blank=True)
    birthday_year = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

