from rest_framework.serializers import ModelSerializer
from EmployeeDirectory.models import Employee

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'profile',
            'first_name',
            'email',
            'last_name',
            'job_title',
            'department',
            'location',
            'hire_date',
            'is_admin',
        ]
