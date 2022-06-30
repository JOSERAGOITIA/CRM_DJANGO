from ast import Or
from audioop import reverse
from email import message
from lzma import FORMAT_AUTO
from multiprocessing import context
from pickle import NONE
from tkinter.messagebox import NO
from tokenize import group
from typing import OrderedDict
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from accounts.models import Customer, Order
from accounts.decorators import unauthenticated_user,allowed_users,admin_only
from .forms import OrderForm,customerForm,CreateUserForm
from .filters import OrderFilter

# Create your views here.

#@unauthenticated_user
def registerPage(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')

            group=Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
                user=user,
            )
            messages.success(request,'Account was created '+ username)
            return redirect('login')
    context={'form':form}
    return render(request,'accounts/register.html',context)

#@unauthenticated_user
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
@admin_only
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
    total_of_members=customers.filter(type='MEMBER').count()
    total_of_mentors=customers.filter(type='MENTOR').count()
    memberpending=orders.filter(status='MemberP').count()
    memberaproved=orders.filter(status='MemberA').count()
    mentorpending=orders.filter(status='MentorP').count()
    mentoraproved=orders.filter(status='MentorA').count()

    context={'orders':orders,'customers':customers,
            'memberpending':memberpending,'memberaproved':memberaproved,'form':form,'mentorpending':mentorpending,
            'formc':formc,'total_of_members':total_of_members,'total_of_mentors':total_of_mentors,'mentoraproved':mentoraproved}
    return render(request,'accounts/dashboard.html',context)

def userPage(request):
    orders=request.user.customer.order_set.all()
    context={'orders':orders}
    return render(request,'accounts/user.html',context)

@login_required(login_url="login")
@allowed_users(allowed_roles=['admin'])
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
@allowed_users(allowed_roles=['admin'])
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
@allowed_users(allowed_roles=['admin'])
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
    
#@login_required(login_url="login")
#@allowed_users(allowed_roles=['admin'])
#def products(request):
#    products=Product.objects.all()
#    return render (request, 'accounts/products.html',{'products':products})

@login_required(login_url="login")
@allowed_users(allowed_roles=['admin'])
def customer(request,pk_test):
    customer=Customer.objects.get(id=pk_test)

    orders=customer.order_set.all()
    orders_count=orders.count()

    tableFilter=OrderFilter(request.GET,queryset=orders)
    orders=tableFilter.qs

    context={'customer':customer,'orders':orders,'orders_count':orders_count,'tableFilter':tableFilter}

    return render(request,'accounts/customer.html',context )


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
    customer = request.user.customer
    form=customerForm(instance=customer)
    if request.method=='POST':
        form=customerForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()

    context={'form':form}
    return render(request, 'accounts/accounts_settings.html', context)

@login_required(login_url='login')
def member(request):

    return render(request,'accounts/member.html')

@login_required(login_url='login')
def mentor(request):
    return render(request,'accounts/mentor.html')

