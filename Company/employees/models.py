from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Employee(models.Model):
    position = models.CharField(max_length= 100)
    salary = models.IntegerField()
    hire_date = models.DateField(auto_now_add= True)
    user = models.OneToOneField(User,
                                on_delete= models.CASCADE)
    department =models.ForeignKey('departments.Department', 
                                  on_delete= models.CASCADE, related_name='employees')
    
    def __str__(self):
        return f"{self.user} {self.position} {self.salary} {self.hire_date} {self.department}"
    