from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.contrib import messages
# Create your views here.

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid:
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created for' + user)
            return redirect('login')
            
    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def loginPage(request):
    
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect!')
            
    context = {}
    return render(request, 'accounts/login.html', context)
    

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

def customer(request, pk):
    customer = Customer.objects.get(id= pk)
    orders = customer.orders_set.all()
    order_count = orders.count()
    context = {'customer': customer,'orders':orders, 'order_count': order_count}
    return render(request, 'accounts/customer.html', context)

def createOrder(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = OrderForm()  # Define form for GET request

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def createCustomer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CustomerForm()

    context = {'form': form}
    return render(request, 'accounts/customer_form.html', context)


def updateOrder(request,pk):
    order = Orders.objects.get(id =pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
   
    context ={'form':form}
    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request,pk):
    order = Orders.objects.get(id =pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context ={'item':order}
    return render(request, 'accounts/delete.html', context)