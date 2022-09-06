from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Products
from .serializers import ProductSerializers


class ProductListApiView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializers

