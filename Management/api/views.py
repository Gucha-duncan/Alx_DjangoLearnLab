from django.shortcuts import render
from django.db.models import Max
from rest_framework.response import Response
from django.http import JsonResponse
from api.serializers import*
from api.models import*
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def product_list(request):
    
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_detail(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def product_update(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
     
    if serializer.is_valid():
        serializer.save() 
    
@api_view(['GET'])
def order_list(request):
    
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def order_detail(request,pk):
    
    orders = Order.objects.get(id=pk)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_info(request):
    products = Product.objects.all()
    serializer = ProductInfoSerializer({
        'products': products,
        'count':len(products),
        'max_price':products.aaggregate(max_price=Max('price'))
    })
    return Response(serializer.data)
