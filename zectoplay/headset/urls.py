from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page, name='main_page'), # http://127.0.0.1:8000
    path('login/', login, name='login'), # http://127.0.0.1:8000/login/
    path('cart/', cart, name='cart'), # http://127.0.0.1:8000/cart/
    path('favourites/', favourites, name='favourites'), # http://127.0.0.1:8000/favourites/
    path('registration/', registration, name='registration'), # http://127.0.0.1:8000/registration/
    path('discounts/', discounts, name='discounts'), # http://127.0.0.1:8000/registration/
    path('reviews/', reviews, name='reviews'), # http://127.0.0.1:8000/registration/
    path('manufacturers/', manufacturers, name='manufacturers'), # http://127.0.0.1:8000/registration/
    path('categories/', categories, name='categories'), # http://127.0.0.1:8000/categories/
]