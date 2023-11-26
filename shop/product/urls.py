from django.urls import path
from product.views import ProductList, DetailView

urlpatterns =[
    path('home/', ProductList.as_view(), name='product-list'),
    path('detail/<str:name>/', DetailView.as_view(), name='detail')
]