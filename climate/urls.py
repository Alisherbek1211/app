from django.urls import path
from .views import ClimateListApiView,ClimateUpdateView,CategoryListApiView,CategoryUpdateView

urlpatterns = [
    path('',ClimateListApiView.as_view()),  
    path('<int:pk>/',ClimateUpdateView.as_view()),  
    path('category/',CategoryListApiView.as_view()),  
    path('category/<int:pk>/',CategoryUpdateView.as_view()),  
]