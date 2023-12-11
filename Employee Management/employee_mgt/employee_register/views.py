from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee
# from django.http import HttpResponse
# Create your views here.
def employeeList(request):
    emp = Employee.objects.all()
    context = {'employee':emp}
    return render(request,'employee_list.html',context)

def employeeForm(request,id=0):
    if request.method == 'GET':
        if id==0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form =EmployeeForm(instance=employee)

        return render(request,'employee_form.html',{'form':form})
    else:
        if id==0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/list')

def employeeDelete(request,id):
    dt = Employee.objects.get(pk=id)
    dt.delete()
    # return HttpResponse('Data deleted successfully')
    return redirect('/list')