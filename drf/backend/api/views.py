from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from products.models import *
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view()
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data ={}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    return Response(data)
