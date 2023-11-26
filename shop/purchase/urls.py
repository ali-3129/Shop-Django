from django.urls import path

from purchase.views import PurchaseAdd, PurchaseList

urlpatterns = [
    path('add/<int:s_id>/', PurchaseAdd.as_view(), name='add-purchase'),
    path('list/<str:user>/', PurchaseList.as_view(), name='list-purchase')
]