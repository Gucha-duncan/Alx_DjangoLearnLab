from django.contrib import admin
from employees.models import Employee, SalaryDetail,Expense
# Register your models here.

admin.site.register(Employee)
admin.site.register(SalaryDetail)
admin.site.register(Expense)