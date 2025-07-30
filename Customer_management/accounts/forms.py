from django.forms import ModelForm
from .models import *

class OrderForm(ModelForm):
    
    class Meta:
        model = Orders
        fields = ('__all__')
        
class CustomerForm(ModelForm):  # ✅ Fixed typo
    class Meta:
        model = Customer
        fields = '__all__'


