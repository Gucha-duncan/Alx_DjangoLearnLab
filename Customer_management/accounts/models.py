from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length= 150, null= True)
    phone = models.IntegerField( null= True)
    email = models.EmailField(max_length= 200, null= True)
    day_created = models.DateTimeField(auto_now_add= True, null = True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    
    PRODUCT_CATEGORY = [
        ('Electronics', 'Electronics'),
        ('Clothing', 'Clothing'),
        ('Home Appliances', 'Home Appliances'),
        ('Books', 'Books'),
        ('Beauty & Personal Care', 'Beauty & Personal Care')
    ]
    
    name = models.CharField(max_length= 100, null = True)
    price = models.FloatField(null= True)
    category = models.CharField(max_length= 200, null = True, choices= PRODUCT_CATEGORY)
    description = models.CharField(max_length= 500, null= True)
    date_created = models.DateTimeField(auto_now_add= True, null= True)
    def __str__(self):
        return self.name
    
class Orders(models.Model):
    ORDER_STATUS = [
        ('pending', 'Pending'),
        ('Delivered', 'Delivered'),
        ('Out for Delivery', 'Out for Delivery'),
    ]
    Customer = models.ForeignKey(Customer, on_delete= models.CASCADE)
    product = models.ManyToManyField(Product, )
    date_created = models.DateTimeField(auto_now_add= True, null= True)
    status = models.CharField(max_length= 500, null= True, choices= ORDER_STATUS)
    def __str__(self):
        return self.status