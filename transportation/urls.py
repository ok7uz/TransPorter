from django.urls import path

from transportation.views import TransportationView, TransportationCreateView

urlpatterns = [
    path('', TransportationView.as_view(), name='transportation-list'),
    path('create/', TransportationCreateView.as_view(), name='transportation-create'),
]