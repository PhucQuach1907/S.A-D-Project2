from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models


class CustomUser(AbstractUser):
    is_normal_user = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

    def clean(self):
        super().clean()
        if not self.username.isalnum():
            raise ValidationError(_('Username must contain only letters and digits.'))
        if len(self.username) < 6:
            raise ValidationError(_('Username must be at least 6 characters.'))
        if len(self.password) < 8:
            raise ValidationError(_('Password must be at least 8 characters.'))
