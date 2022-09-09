from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Phone,Category,Model
from .serializers import PhoneSerializers,CategorySerializers,ModelSerializers


class PhoneListApiView(ListCreateAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializers


class PhoneUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializers


class CategoryListApiView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CategoryUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class ModelListView(ListCreateAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializers


class ModelUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializers
