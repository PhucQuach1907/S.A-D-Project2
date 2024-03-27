from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('', sign_in, name='login'),
    path('register/', sign_up, name='register'),
    path('logout/', sign_out, name='logout'),
    path('profile/', TemplateView.as_view(template_name='login/user_profile.html'), name='user_profile')
]