from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/phone/',include('apelsin.urls')),
    path('api/v1/household/',include('Household.urls')),
    path('api/v1/office/',include('office.urls')),
    path('api/v1/climate/',include('climate.urls')),
    path('api/v1/television/',include('television.urls')),
    path('api/v1/computer/',include('computer.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
