from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Menu

def index(request):
    return HttpResponse("Hello World! This is your restaurant home page")

def menu_detail(request):
    categories = Menu.objects.all()
    output = ""
    for category in categories:
        import pdb; pdb.set_trace()
        items = category.menuitem_set.all()
        output += ', '.join([item.name for item in items])
    return HttpResponse("you are looking at the menu: {}".format(output))