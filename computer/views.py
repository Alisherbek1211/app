from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Computer,Category,Model
from .serializers import ComputerSerializers,CategorySerializers,ModelSerializers


class ComputerListApiView(ListCreateAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializers


class ComputerUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializers


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