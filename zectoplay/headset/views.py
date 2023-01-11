from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *
from django.db import models



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
    'prd_count': prd_count,
}

def main_page(request):
    return render(request, 'headset/index.html', context=content)

def show_category(request, category_name):
    content = {
        'menu': menu,
        'menu_selected': 0,
        'categories': ctgrs.filter(name=category_name),
        'title': 'Zecto Play',
        'prd_count': prd_count,
        'cat_name': category_name
    }
    if category_name == 'mouses':
        filtered_products = products.filter(category_id=1)
        content['products'] = filtered_products
    if category_name == 'keyboards':
        filtered_products = products.filter(category_id=2)
        content['products'] = filtered_products
    if category_name == 'headgears':
        filtered_products = products.filter(category_id=3)
        content['products'] = filtered_products

    return render(request, f'headset/category.html', context=content)
    # return HttpResponse(f'Выбрана категория: {category_name}')

def categories(request):
    return render(request, 'headset/categories.html', context=content)

def discounts(request):
    return HttpResponse('Страница скидок')

def reviews(request):
    return HttpResponse('Страница отзывов')

def manufacturers(request):
    return HttpResponse('Страница производителей')

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

