from django.urls import path

from transportation.views import TransportationView, TransportationCreateView, TransportationUpdateView

urlpatterns = [
    path('', TransportationView.as_view(), name='transportation-list'),
    path('create/', TransportationCreateView.as_view(), name='transportation-create'),
    path('transportation/<int:pk>/update/', TransportationUpdateView.as_view(), name='transportation-update'),
]