from django.urls import path
from .views import DeviceListCreateAPIView, DeviceRetrieveUpdateDestroyAPIView, DeviceLogListCreateAPIView, DeviceLogRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('devices/', DeviceListCreateAPIView.as_view(), name='device-list-create'),
    path('devices/<int:pk>/', DeviceRetrieveUpdateDestroyAPIView.as_view(), name='device-retrieve-update-destroy'),
    path('devicelogs/', DeviceLogListCreateAPIView.as_view(), name='device-log-list-create'),
    path('devicelogs/<int:pk>/', DeviceLogRetrieveUpdateDestroyAPIView.as_view(), name='devicelog-retrieve-update-destroy'),
]
