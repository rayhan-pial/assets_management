from django.urls import path
from .views import CompanyRetrieveUpdateAPIView

urlpatterns = [
    path('company/', CompanyRetrieveUpdateAPIView.as_view(), name='company-detail-update'),
]
