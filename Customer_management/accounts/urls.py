
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name= 'home'),
    path('products/', views.products, name= 'products'),
    path('create_order/', views.createOrder, name= 'create_order'),
    path('create_customer/', views.createCustomer, name="create_customer"),

    path('customer/<str:pk>/', views.customer, name= 'customer')
]
