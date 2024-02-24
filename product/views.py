from django.shortcuts import render
from django.shortcuts import HttpResponse

def products_list(request):
    return render(request, 'product/product_list.html')
