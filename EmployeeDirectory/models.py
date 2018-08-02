from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=40, null=False, blank=True)
    employee_id = models.CharField(max_length=40, null=False, blank=True)
    last_name = models.CharField(max_length=40, null=False, blank=True)
    email = models.CharField(max_length=40, null=False, blank=True)
    job_title = models.CharField(max_length=40, null=True, blank=True)
    department = models.CharField(max_length=40, null=True, blank=True)
    location = models.CharField(max_length=40, null=True, blank=True)
    hire_date = models.DateField(null=True, blank=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name