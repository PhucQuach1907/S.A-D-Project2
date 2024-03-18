from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import AppUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = AppUser
        fields = ('email', 'username')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = AppUser
        fields = ('email', 'username')
