from django.db.models.signals import post_save
from django.dispatch import receiver

from finance.models import paypu
from purchase.models import Purchase


@receiver(post_save, sender=paypu)
def callback(sender, instance, created, **kwargs):
    print("called")
    if instance.payment.is_paid:
        purchase = instance.purchase
        purchase.is_paid = True
        purchase.is_enable = False
        purchase.save()