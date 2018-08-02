from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from EmployeeDirectory.models import Employee
from EmployeeDirectory.serializers import EmployeeSerializer



@method_decorator([login_required], name='dispatch')
class EmployeeList(APIView):
    """
    List all employees, or create a new employee.
    """

    def get(self, request, format=None):
        employees = Employee.objects.all()
        first_name = self.request.query_params.get('first_name', None)

        if first_name:
            employees = Employee.objects.filter(first_name__contains=first_name)
        serializer = EmployeeSerializer(employees, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@method_decorator([login_required], name='dispatch')
class EmployeeDetail(APIView):
    """
    Retrieve, update or delete a employee instance.
    """

    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    

    def put(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

