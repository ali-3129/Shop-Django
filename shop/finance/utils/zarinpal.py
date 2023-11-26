from django.conf import settings
from suds.client import Client


def zpal_request_handler(merchant_id, amount, detail, user_email, phone_num, callback):
    client = Client(settings.ZARRINPAL['gateway_request_url'])
    result = client.service.PaymentRequest(
        merchant_id, amount, detail,
        user_email, phone_num, callback
    )
    if result.Status == 100:
        return 'https://sandbox.zarinpal.com/pg/StartPay/' + result.Authority, result.Authority
    else:
        return None, None


def zpal_checker(merchant_id, amount, authority):
    client = Client(settings.ZARRINPAL['gateway_request_url'])
    result = client.service.PaymentVerification(merchant_id, amount, authority)
    if result.Status in [100, 101]:
        is_paid = True
    else:
        is_paid = False

    return is_paid, result.RefID