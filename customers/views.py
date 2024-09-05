from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from customers.models import Customer



def index(request):
    # counter = len(Customer.objects.all())
    # for i in range(counter):
    #     Customer.objects.get(id=i)
    #     Customer.save()
    all_customers = Customer.objects.all()
    return render(request,'customers/index.html',{'all_customers':all_customers})

def info(request , s):

    customers_info = Customer.objects.get(slug=s)
    # product = get_object_or_404(Product, slug=s)

    return render(request , 'customers/moshtari.html' , context={'info':customers_info})
# Create your views here.
