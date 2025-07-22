from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length= 150)
    description = models.CharField(max_length= 500)
    created_at = models.DateField(auto_now=True)
    head = models.ForeignKey(User, on_delete= models.CASCADE, related_name='leads_department')
    
    def __str__(self):
        return f"{self.name} {self.description} {self.created_at} {self.head}"
    
    