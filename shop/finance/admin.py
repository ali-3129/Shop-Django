from django.contrib import admin
from django.contrib.admin import register

from finance.models import Payment, paypu


@register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount')


@register(paypu)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('purchase', 'payment')
