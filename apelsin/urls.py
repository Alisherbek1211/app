from django.urls import path
from .views import PhoneListApiView,PhoneUpdateView,CategoryListApiView,CategoryUpdateView

urlpatterns = [
    path('',PhoneListApiView.as_view()),  
    path('<int:pk>/',PhoneUpdateView.as_view()),
    path('category/',CategoryListApiView.as_view()),  
    path('category/<int:pk>/',CategoryUpdateView.as_view()),   
]