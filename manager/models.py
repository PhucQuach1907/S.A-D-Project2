from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from django.db import models

from .managers import ManagerUserManager


# Create your models here.
class AppManager(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=50, unique=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True,
                                    related_name='manager_groups')  # Thêm related_name ở đây
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True,
                                              related_name='manager_user_permissions')  # Thêm related_name ở đây

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = ManagerUserManager()

    class Meta:
        db_table = 'app_manager'

    def __str__(self):
        return self.username
