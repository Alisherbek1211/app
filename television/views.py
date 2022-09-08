from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Television,Category
from .serializers import TelevisionSerializers,CategorySerializers


class TelevisionListApiView(ListCreateAPIView):
    queryset = Television.objects.all()
    serializer_class = TelevisionSerializers


class TelevisionUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Television.objects.all()
    serializer_class = TelevisionSerializers


class CategoryListApiView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CategoryUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
