from django.db import models
from django.contrib.auth import get_user_model
from employee.models import Employee

User = get_user_model()

class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    check_out_time = models.DateTimeField()
    check_in_time = models.DateTimeField(null=True, blank=True)
    check_out_condition = models.CharField(max_length=255)
    check_in_condition = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.device} - {self.check_in_condition}"
