from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *


# Register your models here.
@admin.register(AppManager)
class CustomManagerAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = AppManager
    list_display = ('email', 'username',)
    list_filter = ('email', 'username',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
