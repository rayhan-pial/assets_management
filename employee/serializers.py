from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','name', 'designation']
        extra_kwargs={'id':{'read_only':True}}
