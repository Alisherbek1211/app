from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Household,Category,Model
from .serializers import HouseholdSerializers,CategorySerializers,ModelSerializers


class HouseholdListApiView(ListCreateAPIView):
    queryset = Household.objects.all()
    serializer_class = HouseholdSerializers


class HouseholdUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Household.objects.all()
    serializer_class = HouseholdSerializers


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