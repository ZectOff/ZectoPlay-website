from django.urls import path
from headset.views import *
from users.views import *

urlpatterns = [
    path('', main_page, name='main_page'), # http://127.0.0.1:8000
    path('login/', user_login, name='login'), # http://127.0.0.1:8000/login/
    path('cart/', cart, name='cart'), # http://127.0.0.1:8000/cart/
    path('favourites/', favourites, name='favourites'), # http://127.0.0.1:8000/favourites/
    path('registration/', register, name='registration'), # http://127.0.0.1:8000/registration/
    path('discounts/', discounts, name='discounts'), # http://127.0.0.1:8000/registration/
    path('reviews/', reviews, name='reviews'), # http://127.0.0.1:8000/registration/
    path('manufacturers/', manufacturers, name='manufacturers'), # http://127.0.0.1:8000/registration/
    path('categories/', categories, name='categories'), # http://127.0.0.1:8000/categories/
    path('profile/',user_profile,name='user_profile'),
    path('logout/',user_logout,name='logout')
]