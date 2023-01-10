from django import template
from headset.models import *

register = template.Library()

menu = [{'title': 'Категории', 'url_name': 'categories'},
        {'title': 'Скидки', 'url_name': 'discounts'},
        {'title': 'Отзывы', 'url_name': 'reviews'},
        {'title': 'Производители', 'url_name': 'manufacturers'}
]

content = {
    'title': 'Zecto Play'
}

@register.simple_tag(name='g_ctgrs')
def get_categories():
    return Category.objects.all()

@register.simple_tag(name='g_content')
def get_content():
    return content

@register.simple_tag(name='g_menu')
def get_menu():
    return menu

