from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu_list, name='menu_list'),
    path('checkout', views.checkout_detail, name='checkout_detail'),
]