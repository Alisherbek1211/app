from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Climate,Category
from .serializers import ClimateSerializers,CategorySerializers


class ClimateListApiView(ListCreateAPIView):
    queryset = Climate.objects.all()
    serializer_class = ClimateSerializers


class ClimateUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Climate.objects.all()
    serializer_class = ClimateSerializers


class CategoryListApiView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CategoryUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
