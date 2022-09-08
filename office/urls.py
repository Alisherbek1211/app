from django.urls import path
from .views import OfficeListApiView,OfficeUpdateView,CategoryListApiView,CategoryUpdateView

urlpatterns = [
    path('',OfficeListApiView.as_view()),  
    path('<int:pk>/',OfficeUpdateView.as_view()),  
    path('category/',CategoryListApiView.as_view()),  
    path('category/<int:pk>/',CategoryUpdateView.as_view()),  
]