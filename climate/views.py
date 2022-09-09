from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Climate,Category,Model
from .serializers import ClimateSerializers,CategorySerializers,ModelSerializers


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


class ModelListView(ListCreateAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializers


class ModelUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializers
