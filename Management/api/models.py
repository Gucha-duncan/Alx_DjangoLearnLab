from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class User(AbstractUser):
    pass

class Product(models.Model):
    PRODUCT_CATEGORY = [
    ('electronics', 'Electronics'),
    ('books', 'Books'),
    ('fashion', 'Fashion'),
    ('home_kitchen', 'Home & Kitchen'),
    ('beauty_personal_care', 'Beauty & Personal Care'),
    ('sports_outdoors', 'Sports & Outdoors'),
    ('toys_games', 'Toys & Games'),
    ('automotive', 'Automotive'),
    ('grocery_gourmet_food', 'Grocery & Gourmet Food'),
    ('health_household', 'Health & Household'),
]
    name = models.CharField(max_length= 200, null=True)
    description =models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits= 10, decimal_places=2)
    category = models.CharField(max_length=100,blank=True, choices= PRODUCT_CATEGORY)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    
    @property
    def in_stock(self):
        return self.stock > 0
    
    def __str__(self):
        return self.name
    
    
class Order(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'Pending'
        CONFIRMED = 'Confirmed'
        CANCELLED = 'Cancelled'
  
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    product = models.ManyToManyField(Product, through="OrderItem", related_name='orders')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, 
                              choices= StatusChoices.choices, default=StatusChoices.PENDING)
    def __str__(self):
        return f"Order {self.order_id} by {self.user.username}"
    
    
class OrderItem(models.Model):
        order = models.ForeignKey(Order,
                                  related_name='items',
                                  on_delete=models.CASCADE)
        product = models.ForeignKey(Product, on_delete=models.CASCADE)
        quantity = models.PositiveIntegerField()
        
        @property
        def item_subtotal(self):
            return self.product.price * self.quantity
        
        def __str__(self):
            return f"{self.quantity} x {self.product.name} in order {self.order.order_id}"