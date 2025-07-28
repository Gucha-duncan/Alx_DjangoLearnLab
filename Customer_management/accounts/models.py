from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length= 150, null= True)
    phone = models.IntegerField(max_length= 20, null= True)
    email = models.EmailField(max_length= 200, null= True)
    day_created = models.DateField(auto_now_add= True, null = True)

class Product(models.Model):
    
    name = models.CharField(max_length= 100, null = True)
    price = models.FloatField(max_length= 200, null= True)
