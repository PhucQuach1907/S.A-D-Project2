from django.urls import path

from .views import *

urlpatterns = [
    path('image/', search_by_image, name='search_by_image'),
    path('voice/', search_by_voice, name='search_by_voice')
]
