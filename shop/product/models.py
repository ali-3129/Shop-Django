from django.contrib.auth.models import User
from django.db import models


class Type(models.Model):
    type = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.type}"


class Brand(models.Model):
    brand = models.CharField(max_length=32)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='brands', null=True, blank=True)

    def __str__(self):
        return f"{self.brand}"


class Product(models.Model):
    ELECTRONIC = 1
    PODCAST = 2
    BOOK = 3
    CATEGORIES = (
        (ELECTRONIC, 'ELECTRONIC'),
        (PODCAST, 'PODCAST'),
        (BOOK, 'BOOK'),

    )
    name = models.CharField(max_length=32)
    category = models.SmallIntegerField(choices=CATEGORIES, default=ELECTRONIC)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='products')
    is_enable = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE)
    upc = models.CharField(blank=True, null=True, max_length=12)

    def __str__(self):
        return f"{self.name}, {self.upc}"


class Seller(models.Model):
    user = models.ForeignKey(User, related_name='sellers', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return f"{self.user}, {self.phone_number}"


class ProductSeller(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sellers')
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='products')
    price = models.SmallIntegerField(default=0)
    quantity = models.SmallIntegerField(default=1)

    def __str__(self):
        return f"{self.product}, {self.seller}"
