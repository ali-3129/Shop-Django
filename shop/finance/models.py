import uuid

from django.conf import settings
from django.db import models

from purchase.models import Purchase


class Payment(models.Model):
    invoice_number = models.UUIDField(verbose_name=("invoice nummber"), unique=True, default=uuid.uuid4)
    amount = models.PositiveIntegerField(editable=True)
    is_paid = models.BooleanField(default=False)
    payment_log = models.TextField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    authority = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return f"{self.invoice_number, self.is_paid}"


class paypu(models.Model):
    purchase = models.ForeignKey(Purchase, related_name='payments', null=True, blank=True, on_delete=models.RESTRICT)
    payment = models.ForeignKey(Payment, related_name='purschases', null=True, blank=True, on_delete=models.SET_NULL)

