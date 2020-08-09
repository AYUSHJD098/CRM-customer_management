from django.shortcuts import render
from django.http import HttpResponse
from .models import  *


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
	order_count = Order.count()	
	return render(request, 'accounts/customer.html', {'orders':order, 'customer':customer, 'order_count':order_count})  

def products(request):
	products = Product.objects.all()
	return render(request, 'accounts/products.html', {'products':products})


