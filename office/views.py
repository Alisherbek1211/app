from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Office,Category,Model
from .serializers import OfficeSerializers,CategorySerializers,ModelSerializers


class OfficeListApiView(ListCreateAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializers


class OfficeUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializers


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