from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name='home_clothes.html'), name='home_clothes'),
    path('clothes/<int:pk>/', ClothesViewAPI.as_view({'post': 'add_to_cart'}), name='add-to-cart'),
]
