from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *


menu = [{'title': 'Категории', 'url_name': 'categories'},
        {'title': 'Скидки', 'url_name': 'discounts'},
        {'title': 'Отзывы', 'url_name': 'reviews'},
        {'title': 'Производители', 'url_name': 'manufacturers'}
]

products = Headset.objects.all()
prd_count = len(products)
ctgrs = Category.objects.all()
content = {
    'products': products,
    'menu': menu,
    'menu_selected': 0,
    'categories': ctgrs,
    'title': 'Zecto Play',
    'prd_count': prd_count
}

def main_page(request):
    return render(request, 'headset/index.html', context=content)

def categories(request):
    return render(request, 'headset/categories.html', context=content)

def discounts(request):
    return HttpResponse('Страница скидок')

def reviews(request):
    return HttpResponse('Страница отзывов')

def manufacturers(request):
    return HttpResponse('Страница производителей')

def login(request):
    return render(request, 'headset/login.html', context=content)

def registration(request):
    return render(request, 'headset/registration.html', context=content)

def cart(request):
    return render(request, 'headset/cart.html', context=content)

def favourites(request):
    return render(request, 'headset/favourites.html', context=content)

def headsets(request):
    if (request.GET):
        print(request.GET)

    return HttpResponse("<h1 align=center>Наборы гарнитуры</h1>\n<h2 align=center>"
                        "Наборчики гарнитуры какой-то</h2>")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1 align=center>Такой страницы нет</h1>\n<h2 align=center>"
                        "Мне жаль тебя мага</h2>")

