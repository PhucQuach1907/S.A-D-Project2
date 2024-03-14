from django.urls import path, include
from rest_framework.routers import DefaultRouter

from book.views import *
from mobile.views import *
from cart.views import *
from search.views import *

router = DefaultRouter()
router.register(r'books', BookViewAPI)
router.register(r'mobiles', MobileViewAPI)
router.register(r'cart-items', CartViewAPI)

urlpatterns = [
    path('', include(router.urls)),
    path('search-book/', SearchBookAPI.as_view(), name='search-book'),
    path('search-mobile/', SearchMobileAPI.as_view(), name='search-mobile'),
]
