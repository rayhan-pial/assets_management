from rest_framework import generics, permissions
from .models import Company
from .serializers import CompanySerializer

class CompanyRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Company.objects.filter(user=self.request.user)
