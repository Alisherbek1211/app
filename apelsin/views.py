from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Phone
from .serializers import PhoneSerializers


class PhoneListApiView(ListCreateAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializers


class PhoneUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializers

