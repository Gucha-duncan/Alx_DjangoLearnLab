from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length= 100)
    code = models.IntegerField()
    number = models.BigIntegerField()
    date_created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)