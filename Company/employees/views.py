from django.shortcuts import render, redirect
from .models import Employee,SalaryDetail, Expense
from .forms import EmployeeForm, SalaryForm, ExpenseForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def create_employee(request):
    
    if request.method == "POST":
        employee_form = EmployeeForm(request.POST)
        salary_form = SalaryForm(request.POST)
        
        if employee_form.is_valid() and salary_form.is_valid():
            employee = employee_form.save(commit= False)
            employee.user = request.user 
            employee.save()
            
            salary = salary_form.save(commit = False)
            salary.employee = employee  
            salary.save()
            
            return redirect('employee_detail', employee.id)
    
    else:
        employee_form = EmployeeForm()
        salary_form = SalaryForm()
        
    return render(request, 'employees/create_employee.html' ,
                  {"employee_form":employee_form, "salary_form":salary_form})
         
@login_required
def employee_detail(request, pk):
    employee = Employee.objects.get(pk=pk)
    salary = SalaryDetail.objects.get(employee=employee)
    expenses =  Expense.objects.filter(employee=employee)
    
    total_expenses = sum(e.amount for e in expenses)
    net_income = salary.total_earnings() - total_expenses
    weekly_income = net_income // (salary.months_worked * 4)
    
    return render(
        request, 'employees/employee_detail.html',
        {
            'employee':employee,
            'salary':salary,
            'net_income': net_income,
            'weekly_income':weekly_income
        }
    )