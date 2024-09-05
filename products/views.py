from itertools import product

from django.db.models import Avg, Max, Min
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string

from products.models import Product


def show_product(request):
    # all_products = Product.objects.all().order_by('price')
    all_products = Product.objects.all().order_by('-price')
    num_products = Product.objects.all().count()
    info = all_products.aggregate(Avg('price') , Max('price') , Min('price'))

    return render(request, 'products/product_list.html', {'products': all_products, 'pro_num': num_products , 'info':info})


def show_details(request, num):
    if num == 0 or num > Product.objects.all().count():
        return HttpResponse(f"محصول یافت نشد")
    else:
        product = Product.objects.get(id=num)

        # return render(request, 'products/IphoneDetails.html', {'product': product})
        return HttpResponseRedirect(f'/product/{product.title}')


def show_mobile(request, mobile):
    mobiles = Product.objects.get(title=mobile)
    return render(request, 'products/IphoneDetails.html', {'mobile': mobiles})


def ViewProductdetails(request, s):
    # product = Product.objects.get(slug=s)
    product = get_object_or_404(Product, slug=s)  # یک تابع دیگه برای انجام کار تابع بالاس
    return render(request, 'products/IphoneDetails.html', context={'mobile': product})

# Create your views here.
