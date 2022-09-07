from django.urls import path
from .views import PhoneListApiView,PhoneUpdateView

urlpatterns = [
    path('phone/',PhoneListApiView.as_view()),  
    path('phone/<int:pk>/',PhoneUpdateView.as_view()),  
]