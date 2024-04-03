from django.urls import path
from .views import EmployeeListCreateAPIView, EmployeeRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('employees/', EmployeeListCreateAPIView.as_view(), name='employee-list-create'),
    path('employee/<int:pk>/', EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='employee-retrieve-update-destroy'),
]
