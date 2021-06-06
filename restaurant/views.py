from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Menu

def index(request):
    return render(request, 'restaurant/index.html')

def menu_detail(request):
    categories = Menu.objects.all()
    menu = {}
    for category in categories:
        items = category.menuitem_set.all()
        menu[category.name] = items

    context = {"menu": menu, "title": "Menu"}
    return render(request, 'restaurant/menu.html', context)


def checkout_detail(request):
    context = {"title": "Checkout"}
    return render(request, "restaurant/checkout.html", context)