from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Employee(models.Model):
    EMPLOYEE_TYPE_CHOICES = [
        ('full', 'Full Time'),
        ('part', 'Part Time'),
        ('other', 'other')
        
    ]

    user = models.OneToOneField(User,
                                on_delete= models.CASCADE)
    name = models.CharField(max_length= 100)
    age = models.PositiveIntegerField()
    position = models.CharField(max_length= 100)
    employee_type = models.CharField(max_length= 100)
    
    hire_date = models.DateField(auto_now_add= True)
    department =models.ForeignKey('departments.Department', 
                                  on_delete= models.CASCADE, related_name='employees')
    
    def __str__(self):
        return f"{self.user} {self.position}  {self.department}"
    
class SalaryDetail(models.Model):
        employee = models.OneToOneField(Employee, on_delete= models.CASCADE )
        monthly_salary = models.FloatField()
        months_worked = models.PositiveIntegerField()
        bonus_percent = models.FloatField()
        
        def total_earnings(self):
            
            return self.monthly_salary * self.months_worked
        def bonus_amount(self):
            
            return (self.bonus_percent / 100) * self.total_earnings()
        
        def net_income(self):
            return self.total_earnings() + self.bonus_amount()
        
class Expense(models.Model):
    employee = models.ForeignKey(Employee, on_delete= models.CASCADE, related_name= 'expenses')
    name = models.CharField(max_length= 150)
    amount = models.FloatField()
    
    