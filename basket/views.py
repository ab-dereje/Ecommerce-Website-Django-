from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from store.models import Product
from .basket import Basket

# Create your views here.
def basket_summary(request):
    basket = Basket(request)
    return render(request, 'store/basket/summary.html',{'basket': basket})

def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action')=='post':
        product_id = int(request.POST.get('productid'))
        product_qty = (request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product,qty=product_qty)
        response = JsonResponse({'qty':product_qty})
        return response
