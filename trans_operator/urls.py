from django.urls import path

from trans_operator.views import OperatorListView, OperatorCreateView, OperatorDeleteView

urlpatterns = [
    path('operators/', OperatorListView.as_view(), name='operator-list'),
    path('operators/create/', OperatorCreateView.as_view(), name='operator-create'),
    path('operators/<int:pk>/delete/', OperatorDeleteView.as_view(), name='operator-delete'),
]