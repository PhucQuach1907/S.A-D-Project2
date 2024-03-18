from django.urls import path

from .views import *

urlpatterns = [
    path('voice/', search_by_voice, name='search_by_voice')
]
