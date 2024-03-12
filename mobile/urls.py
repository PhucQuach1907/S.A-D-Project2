from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeMobileView, name='home_mobile'),
    # path('add/<int:book_id>/', add_to_cart, name='add_to_cart'),
]
