from django.contrib import admin

# Register your models here.
from .models import Store, Menu, Order

admin.site.register(Store)
admin.site.register(Menu)
admin.site.register(Order)
