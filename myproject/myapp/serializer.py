from rest_framework import serializers
from .models import Department , Employee
class Deptserializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
class Empserializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'