from rest_framework import serializers
from .models import Device, DeviceLog
from employee.models import Employee

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'name', 'description', 'updated_at']
        read_only_fields = ['id', 'updated_at']


class DeviceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceLog
        fields = ['id', 'device', 'employee', 'check_out_time', 'check_in_time', 'check_out_condition', 'check_in_condition']
        read_only_fields = ['id', 'check_out_condition']

    def validate(self, data):

        device_id = data.get('device')

        if not Device.objects.filter(pk=device_id).exists():
            raise serializers.ValidationError("Invalid device ID.")

        employee_id = data.get('employee')

        if not Employee.objects.filter(pk=employee_id).exists():
            raise serializers.ValidationError("Invalid employee ID.")


        check_out_time = data.get('check_out_time')
        check_in_time = data.get('check_in_time')

        if check_in_time < check_out_time:
            raise serializers.ValidationError("Check-in time cannot be before check-out time.")

        return data
