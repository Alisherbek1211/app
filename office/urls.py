from django.urls import path
from .views import OfficeListApiView,OfficeUpdateView,CategoryListApiView,CategoryUpdateView,ModelListView,ModelUpdateView

urlpatterns = [
    path('',OfficeListApiView.as_view()),  
    path('<int:pk>/',OfficeUpdateView.as_view()),  
    path('category/',CategoryListApiView.as_view()),  
    path('category/<int:pk>/',CategoryUpdateView.as_view()), 
    path('model/',ModelListView.as_view()),  
    path('model/<int:pk>/',ModelUpdateView.as_view()), 
]