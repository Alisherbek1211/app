from django.urls import path
from .views import TelevisionListApiView,TelevisionUpdateView,CategoryListApiView,CategoryUpdateView

urlpatterns = [
    path('',TelevisionListApiView.as_view()),  
    path('<int:pk>/',TelevisionUpdateView.as_view()),  
    path('category/',CategoryListApiView.as_view()),  
    path('category/<int:pk>/',CategoryUpdateView.as_view()),  
]