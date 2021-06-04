from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone


class Store(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', 
                    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], 
                                    max_length=17, blank=True) # validators should be a list

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=100)
    picture = models.ImageField(default='default.jpg', upload_to='menu_items')

    def __str__(self):
        return self.name


class Order(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', 
                    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], 
                                    max_length=17, blank=True) # validators should be a list
    order_date = models.DateTimeField('order date')

    def __str__(self):
        return self.first_name

    def get_order_sum(self):
        sum = 0
        for item in self.orderitem_set.all():
            sum += (item.price * item.quantity)
        return sum


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
