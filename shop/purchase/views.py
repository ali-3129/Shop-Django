from django.db.models import Sum, F, Q
from django.shortcuts import render, redirect
from django.views import View

from product.models import ProductSeller
from purchase.forms import IForm
from purchase.models import Purchase


class PurchaseAdd(View):
    def get(self, request, s_id):
        product = ProductSeller.objects.get(id=s_id)
        form = IForm()
        return render(request, 'purchase/add.html', {'product': product, 'form': form})

    def post(self, request, s_id, *args, **kwargs):
        product = ProductSeller.objects.get(id=s_id)

        form = IForm(request.POST)
        instance = form.save(commit=False)
        instance.user = request.user
        instance.product_seller = product
        instance.save()

        return render(request, 'purchase/added.html', {'product':product})


class PurchaseList(View):
    def get(self, request, user):
        purchase = Purchase.objects.filter(Q(user=request.user) and Q(is_enable=True))
        if purchase:

            total = purchase.aggregate(price=Sum(F('product_seller__price')*F('quantity')))
            p = int(total['price'])
        else:
            p = 0
        return render(request, 'purchase/list.html',
                      {'purchases': purchase, 'total': p})


