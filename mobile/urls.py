from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name='home_mobile.html'), name='home_mobile'),
    path('mobiles/<int:pk>/', MobileViewAPI.as_view({'post': 'add_to_cart'}), name='add-to-cart'),
]
