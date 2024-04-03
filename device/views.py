# views.py
from rest_framework import generics, permissions
from .models import Device, DeviceLog
from .serializers import DeviceSerializer, DeviceLogSerializer

class DeviceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DeviceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class DeviceLogListCreateAPIView(generics.ListCreateAPIView):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(employee__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save()


class DeviceLogRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DeviceLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        device_id = self.kwargs['pk']
        return DeviceLog.objects.filter(device=device_id)
