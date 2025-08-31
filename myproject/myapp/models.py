from django.db import models

# Create your models here.
class Department(models.Model):
    dept_id = models.BigAutoField(primary_key=True)
    dept_name = models.CharField(max_length=100)
    dept_code = models.CharField(max_length=10, unique=True)
    status = models.BooleanField(default=True)

class Employee(models.Model):
    emp_id = models.BigAutoField(primary_key=True)
    emp_name = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=10, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE , related_name='employees')
    status = models.BooleanField(default=True)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
