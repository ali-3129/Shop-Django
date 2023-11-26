from django.contrib import admin
from django.contrib.admin import register

from product.models import Product, Seller, ProductSeller, Type, Brand


@register(Type)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['type']



@register(Brand)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['brand']


@register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'get_category_display']


@register(Seller)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number']


@register(ProductSeller)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'seller', 'price', 'quantity']



