from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render ,redirect
from .models import *
from .forms import *
from django.db.models import Sum

# Create your views here.
def home(request):
    return render(request,'home.html')

def deptlist(request):
    department=Department.objects.all()
    data={'department':department}
    return render(request,'deptlist.html',data)

def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('deptlist')
    else:
        form = DepartmentForm()

    return render(request, 'dept_form.html', {'form': form, 'form_title': 'Add Department'})

def department_detail(request, pk):
    department = get_object_or_404(Department, id=pk)
    return render(request, 'dept_view.html', {'department': department})

def edit_department(request,pk):
    department = get_object_or_404(Department, id=pk)

    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('deptlist')
    else:
        form = DepartmentForm(instance=department)

    return render(request, 'dept_form.html', {'form': form, 'form_title': 'Edit Department'})

def delete_department(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    department.delete()
    return redirect('deptlist')

#Employee Module Start
def emplist(request):
    Emp=Employee.objects.all()
    data={'emp':Emp}
    return render(request,'emp_list.html',data)

def add_employee(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('emplist')
    return render(request, 'emp_form.html', {'form': form, 'form_title': 'Add Employee'})

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, id=pk)
    return render(request, 'emp_view.html', {'employee': employee})

def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        # Redirect to the employee list or another appropriate page
    return render(request, 'emp_form.html', {'form': form, 'form_title': 'Edit Employee'})

def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()
    return redirect('emplist')


#Salary Module Start

def salary_list(request):
    salary_entries = EmployeeSalary.objects.all()
    return render(request, 'salary_list.html', {'salary_entries': salary_entries})

def salary_detail(request, entry_id):
    salary_entry = get_object_or_404(EmployeeSalary, id=entry_id)
    return render(request, 'salary_view.html', {'salary_entry': salary_entry})

def add_salary_entry(request):
    if request.method == 'POST':
        form = SalaryEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('salary_list')
    else:
        form = SalaryEntryForm()

    return render(request, 'salary_form.html', {'form': form, 'form_title': 'Add Salary Entry'})

def edit_salary_entry(request, entry_id):
    salary_entry = get_object_or_404(EmployeeSalary, id=entry_id)

    if request.method == 'POST':
        form = SalaryEntryForm(request.POST, instance=salary_entry)
        if form.is_valid():
            form.save()
            return redirect('salary_list')
    else:
        form = SalaryEntryForm(instance=salary_entry)

    return render(request, 'salary_form.html', {'form': form, 'form_title': 'Edit Salary Entry'})

def salary_report(request):
    department_salary_dict = {}
    start_date=request.POST.get('sdate')
    end_date=request.POST.get('edate')
    start_date = '2024-01-01' 
    end_date = '2024-12-31' 

    salary_entries = EmployeeSalary.objects.filter(start_date__gte=start_date, end_date__lte=end_date)
    print(salary_entries)

    for entry in salary_entries:
        department = entry.employee.department.name 
        total_salary = department_salary_dict.get(department, 0) + entry.salary
        department_salary_dict[department] = total_salary
    
    return render(request, 'salary_report.html', {'department_salary_dict': department_salary_dict})



def department_hierarchy(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    hierarchy = generate_department_hierarchy(department)

    return render(request, 'dept_hierachy.html', {'department': department, 'hierarchy': hierarchy})

def generate_department_hierarchy(department):
    hierarchy = {}

    manager = Employee.objects.filter(department=department, designation='Manager').first()

    if manager:
        hierarchy['manager'] = {'employee': manager, 'subordinates': []}

        tls = Employee.objects.filter(department=department, reporting_manager=manager, designation='TL')

        for tl in tls:
            hierarchy[tl.id] = {'employee': tl, 'subordinates': []}

            associates = Employee.objects.filter(department=department, reporting_manager=tl, designation='Associate')
            hierarchy[tl.id]['subordinates'] = associates

    return hierarchy