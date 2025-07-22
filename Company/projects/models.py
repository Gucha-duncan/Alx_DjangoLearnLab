from django.db import models
from employees.models import Employee

# Create your models here.
class Project(models.Model):
    
    name = models.CharField(max_length= 150)
    description = models.CharField(max_length= 200)
    start_date = models.DateField(auto_now_add= True)
    status = models.CharField(max_length= 50)
    end_date = models.DateField(auto_now= True)
    manager = models.ManyToManyField(Employee)
    
    def __str__(self):
        return f"{self.name}{self.description} {self.start_date} {self.status} {self.end_date} {self.manager}"
        
    
    
   




