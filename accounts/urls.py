from django.urls import path
from accounts import views


urlpatterns = [
    path('', views.home, name="home"),
    path('customer/<str:pk>', views.customer, name="customer"),
    path('products/', views.products, name='product'),
    path('addorder/', views.create_order, name='create_order'),
    path('addcustomer/', views.create_customer, name='create_customer')
]
