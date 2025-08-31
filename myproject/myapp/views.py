from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Department , Employee
from .serializer import Deptserializer , Empserializer
# Create your views here.
from datetime import date ,datetime
class Deptview(APIView):
    def get(self , request):
        dept = Department.objects.filter(status=True).all().order_by('dept_id')
        serializer = Deptserializer(dept,many=True)
        return Response(serializer.data)
    def post(self, request):
        payload = request.data
        payload['status'] = True
        serializer  = Deptserializer(data=payload)
        if serializer.is_valid():
            serializer.save()
        return Response({'department added successfully !!!'})
    
class Empview(APIView):
    def get(self , request):
        emp = Employee.objects.filter(status=True).all().order_by('emp_id')
        # empdata =Employee.objects.filter(department=1).all()
        # for i in empdata:
        #     print('empdt:>>>>>>>>>>>>>>>>>',i.department.dept_name)
        # emp = Employee.objects.all()
        print(emp)
        serializer  = Empserializer(emp , many=True)
        return Response(serializer.data)
    def post(self, request):
        payload = request.data
        payload['status'] = True
        payload['hire_date'] = date.today()
        serializer = Empserializer(data = payload)
        if serializer.is_valid():
            print('save in progress...')
            serializer.save()
            return Response(serializer.data)
            # return Response({'employee added successfully !!!'})
        else:
            print(serializer.errors)
            return Response({'error': 'Employee creation failed', 'details': serializer.errors}, status=400)
