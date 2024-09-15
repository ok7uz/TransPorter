from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('transportation.urls')),
    path('', include('auth.urls')),
    path('', include('trans_operator.urls')),
]
