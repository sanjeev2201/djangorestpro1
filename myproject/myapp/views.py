from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Department , Employee
from .serializer import Deptserializer , Empserializer
# Create your views here.

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
        return Response({'employee added successfully !!!'})
