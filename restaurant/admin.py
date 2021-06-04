from django.contrib import admin

# Register your models here.
from .models import Store, Menu, MenuItem, Order, OrderItem

class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 3


class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 3


class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal Infomation', {'fields': ['first_name', 'last_name', 'email', 'phone_number'], 'classes': ['collapse']})
    ]
    inlines = [OrderItemInline]


admin.site.register(Store)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Order, OrderAdmin)
