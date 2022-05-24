from ast import Or
from audioop import reverse
from email import message
from lzma import FORMAT_AUTO
from multiprocessing import context
from pickle import NONE
from tkinter.messagebox import NO
from typing import OrderedDict
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


from accounts.models import Customer, Order, Product
from .forms import OrderForm,customerForm,CreateUserForm
from .filters import OrderFilter

# Create your views here.

def registerPage(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created '+ user)
            return redirect('login')
    context={'form':form}
    return render(request,'accounts/register.html',context)

def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return  redirect('home')
        else: 
            messages.info(request,'Username OR Password is incorrect')
    context={}
    return render(request,'accounts/login.html',context)

def logoutUser(request):
    logout(request)
    return render('accounts/login.html')

@login_required(login_url="login")
def home(request):
    #formulario creat order
    form=OrderForm()
    formc=customerForm()
    ## para actualizar 
    if request.method== 'POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
    if request.method=='POST':
        formc=customerForm(request.POST)
        if formc.is_valid():
            formc.save()
    form=OrderForm()
    formc=customerForm()
    #table 
    orders=Order.objects.all()
    customers=Customer.objects.all()
    #status cont
    total_customer=customers.count()
    total_orders=orders.count()
    delivered=orders.filter(status='Delivered').count()
    pending=orders.filter(status='Pending').count()
    context={'orders':orders,'customers':customers,'total_orders':total_orders,
            'delivered':delivered,'pending':pending,'form':form,
            'formc':formc}
    return render(request,'accounts/dashboard.html',context )

@login_required(login_url="login")
def updateorder(request,pk_update):
    order=Order.objects.get(id=pk_update)
    form=OrderForm(instance=order)
    if request.method=='POST':
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'accounts/order_form.html',context )

@login_required(login_url="login")
def delateorder(request,pk_delate):
    order=Order.objects.get(id=pk_delate)
    form=OrderForm(instance=order)
    if request.method=='POST':
        form=OrderForm(request.POST,instance=order)
        order.delete()
        return redirect('/')
    context={'item':order,'form':form}
    return render(request,'accounts/delate.html',context )

@login_required(login_url="login")
def creatnewordercu(request,pk_creatorder):
    customer=Customer.objects.get(id=pk_creatorder)
    form=OrderForm(initial={'customer':customer})
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'accounts/createorder.html',context)
    
@login_required(login_url="login")
def products(request):
    products=Product.objects.all()
    return render (request, 'accounts/products.html',{'products':products})

@login_required(login_url="login")
def customer(request,pk_test):
    customer=Customer.objects.get(id=pk_test)

    orders=customer.order_set.all()
    orders_count=orders.count()

    tableFilter=OrderFilter(request.GET,queryset=orders)
    orders=tableFilter.qs

    context={'customer':customer,'orders':orders,'orders_count':orders_count,'tableFilter':tableFilter}

    return render(request,'accounts/customer.html',context )




