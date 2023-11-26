from django.contrib.auth.models import User
from django.db import models

from product.models import ProductSeller


class Purchase(models.Model):
    user = models.ForeignKey(User, related_name='purchases', on_delete=models.CASCADE)
    product_seller = models.ForeignKey(ProductSeller, related_name='purchases', on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    quantity = models.SmallIntegerField(default=1)
    is_enable = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user}"

