from django.shortcuts import render
from django.http import HttpResponse
from .models import  *


def home(request):
	order = Order.objects.all()
	customer = Customer.objects.all()

	total_customer =  Customer.objects.count()
	total_order = Order.objects.count()
	delivered = Order.objects.filter('Delivered').count()
	pending = Order.objects.filter('Pending').count()

	context = { 'orders':order , 'customers':customer,'total_customer' : total_customer,'total_order' : total_order,'delivered' : delivered,'pending': pending		}

	return render(request, 'accounts/dashboard.html', context)

def customer(request):
	
	return render(request, 'accounts/customer.html')

def products(request):
	products = Product.objects.all()
	return render(request, 'accounts/products.html', {'products':products})


