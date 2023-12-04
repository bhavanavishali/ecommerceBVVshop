from django.shortcuts import get_object_or_404, render
from .models import Product,Category

# Create your views here.


def allProCat(request,c_slug=None):
    c_page = None
    products = None
    if c_slug!= None:
        c_page = get_object_or_404(Category,slug=c_slug)
        products = Product.objects.all().filter(category=c_page,available=True)
    else:
        products = Product.objects.all().filter(available=True)
    return render(request,'category.html',{'products':products,'category':c_page})

def proDetails(request,c_slug,product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product})