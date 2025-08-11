from django.urls import path
from .import views

urlpatterns = [
    path('products/', views.product_list, name='product-list'),
    path('product/detail/<str:pk>/', views.product_detail, name='product-detail'),
    path('orders/', views.order_list, name='order-list'),
     path('products/info/', views.product_info, name='product-info'),
]
