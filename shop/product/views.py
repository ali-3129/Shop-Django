from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from product.models import Product, ProductSeller
from purchase.forms import IForm


class ProductList(ListView):
    model = Product
    template_name = 'product/list.html'


class DetailView(View):

    def get(self, request, name):
        product = ProductSeller.objects.filter(product__name=name)
        form = IForm()
        return render(request, 'product/detail.html', {'product': product, 'form': form})

    # def post(self, request, name, *args, **kwargs):
    #     p = ProductSeller.objects.filter(product__name=name)
    #     product = int(request.POST['product_seller'])
    #     form = IForm(request.POST)
    #     instance = form.save(commit=False)
    #     instance.user = request.user
    #     instance.quantity = int(request.POST['quantity'])
    #     instance.product_seller = p.filter(id=product).first()
    #     return render(request, 'product/detail.html', {'form':form})





