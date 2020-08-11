from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import  *
from .forms import *
from django.forms import inlineformset_factory
from .filters import  OrderFilter
from django.contrib.auth.forms import UserCreationForm


def home(request):
	order = Order.objects.all()
	customer = Customer.objects.all()

	total_customer =  Customer.objects.count()
	total_order = Order.objects.count()
	delivered = order.filter(status='Delivered').count()
	pending = order.filter(status='Pending').count()

	context = { 'orders':order , 'customers':customer,'total_customer' : total_customer,'total_order' : total_order, 'delivered' : delivered, 'pending' : pending}

	return render(request, 'accounts/dashboard.html', context)

def customer(request, pk):
	customer = Customer.objects.get(id=pk)
	order = customer.order_set.all()
	myfilter = OrderFilter(request.GET, queryset=order)
	order = myfilter.qs
	order_count = customer.order_set.count()	
	return render(request, 'accounts/customer.html', {'myfilter':myfilter, 'orders':order, 'customer':customer, 'order_count':order_count})  

def products(request):
	products = Product.objects.all()
	return render(request, 'accounts/products.html', {'products':products})


def create_order(request, pk):
	OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10 )
	customer = Customer.objects.get(id=pk)
	formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
	#form = OrderForm(initial={'customer':customer})
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		#form = OrderForm(request.POST)
		formset = OrderFormSet(request.POST, instance=customer)
		if formset.is_valid():
			formset.save()
			return redirect('/')

	context = {'form':formset}
	return render(request, 'accounts/order_form.html', context)


def update_order(request, pk):
	
	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)
	if request.method == 'POST':	
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect("/")

	context = {"form":form, 'order':order}
	return render(request, 'accounts/order_form.html', context)


def create_customer(request):

	form = CustomerForm()
	if request.method == 'POST':
		form = CustomerForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/")
	context = {"form":form}
	return render(request, 'accounts/customer_form.html', context)


def delete_order(request, pk):
	order = Order.objects.get(id=pk)
	if request.method =='POST':
		order.delete()
		return redirect('/')
	context = {'order':order}
	return render(request,'accounts/delete.html', context)





                      
def register(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			
			form.save()
	context = {'form':form}
	return render(request, 'accounts/register.html', context)

def login(request):
	context = {}
	return render(request, 'accounts/login.html')