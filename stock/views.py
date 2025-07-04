from django.shortcuts import render
from .models import Product


def home(request):
    return render(request, 'stock/home.html')


def about(request):
    return render(request, 'stock/about.html')


def contact(request):
    return render(request, 'stock/contact.html')


def product(request):
    products = Product.objects.all().order_by('id')
    return render(request, 'stock/product.html', {'products': products})
