from django.db import models

# Create your models here.
class Manager(models.Model):
    name = models.CharField(max_length=128, unique=True)
    
class Employee(models.Model):
    name = models.CharField(max_length=128, unique=True)
    manager_name = models.ForeignKey(Manager, on_delete=models.CASCADE)
    
class Client(models.Model):
    name = models.CharField(max_length=128, unique=True)
    salary = models.IntegerField()
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    employee_name = models.ForeignKey(Employee, on_delete=models.CASCADE)

class EmployeeRequest(models.Model):
    employee_name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now_add=True)
    field_name = models.CharField(max_length=128)
    previous_value = models.CharField(max_length=128)
    new_value = models.CharField(max_length=128)
    status = models.CharField(max_length=20)
