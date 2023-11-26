from django.db.models import Sum, F, Q
from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings

from finance.models import Payment, paypu
from finance.utils.zarinpal import zpal_request_handler, zpal_checker
from purchase.models import Purchase


class PayView(View):
    def get(self, request, *args, **kwargs):

        payment_link, authority = zpal_request_handler(
            settings.ZARRINPAL['merchant_id'], kwargs['p'], "einkauf", 'ali.250.asghari@gmial.com', None,
            settings.ZARRINPAL['gateway_callback_url']
        )
        if payment_link is not None:
            print(payment_link)
            return redirect(payment_link)


class VerifyView(View):
    def get(self, request, *args, **kwargs):
        purchase = Purchase.objects.filter(Q(user=request.user) and Q(is_enable=True))
        total = purchase.aggregate(price=Sum(F('product_seller__price') * F('quantity')))
        p = int(total['price'])
        authority = request.GET.get('Authority')
        is_paid, ref_id = zpal_checker(
            merchant_id=settings.ZARRINPAL['merchant_id'], amount=p, authority=authority
        )
        is_paid = request.GET.get('Status')
        if is_paid == 'NOK':
            is_paid=False
        else:
            is_paid=True
        pay = Payment.objects.create(amount=p, is_paid=is_paid, payment_log="", user=request.user, authority=authority)
        for pp in purchase:
            paypu.objects.create(payment=pay, purchase=pp)

        return render(request, 'pay/verify.html', {'ref_id': ref_id, 'is_paid': is_paid})
