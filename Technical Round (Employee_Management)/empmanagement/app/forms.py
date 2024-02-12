from django import forms
from .models import *

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DepartmentForm, self).__init__(*args, **kwargs)

class SalaryEntryForm(forms.ModelForm):
    class Meta:
        model = EmployeeSalary
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SalaryEntryForm, self).__init__(*args, **kwargs)