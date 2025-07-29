from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    orders = Orders.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = Orders.objects.filter(status='Delivered').count()
    pending = Orders.objects.filter(status='Pending').count()
    
    context = {'orders': orders, 'customers':customers, 'delivered':delivered, 'pending':pending, 'total_customers': total_customers, 'total_orders': total_orders}
    return render(request, 'accounts/dashboard.html',context)

def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html',{'products':products})

def customer(request):
    return render(request, 'accounts/customer.html')



