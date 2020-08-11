from django.urls import path
from accounts import views


urlpatterns = [
    path('', views.home, name="home"),
    path('customer/<str:pk>/', views.customer, name="customer"),
    path('products/', views.products, name='product'),
    path('add_order/<str:pk>/', views.create_order, name='create_order'),
    path('update_order/<str:pk>/', views.update_order, name='update_order'),
    path('delete_order/<str:pk>/', views.delete_order, name='delete_order'),
    path('add_customer/', views.create_customer, name='create_customer'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]
