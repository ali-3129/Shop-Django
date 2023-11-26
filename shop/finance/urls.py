from django.urls import path
from finance.views import PayView, VerifyView
urlpatterns = [
    path('pay/<int:p>/', PayView.as_view(), name='pay-v'),
    path('verify/', VerifyView.as_view(), name='verify')
]