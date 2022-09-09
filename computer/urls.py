from django.urls import path
from .views import ComputerListApiView,ComputerUpdateView,CategoryListApiView,CategoryUpdateView,ModelListView,ModelUpdateView

urlpatterns = [
    path('',ComputerListApiView.as_view()),  
    path('<int:pk>/',ComputerUpdateView.as_view()),  
    path('category/',CategoryListApiView.as_view()),  
    path('category/<int:pk>/',CategoryUpdateView.as_view()),  
    path('model/',ModelListView.as_view()),  
    path('model/<int:pk>/',ModelUpdateView.as_view()), 
]