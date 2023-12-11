from django.urls import path
from employee_register import views
urlpatterns = [
   path('',views.employeeForm,name='employeeinsert'),
   path('list',views.employeeList,name='employeelist'),
   path('<int:id>/',views.employeeForm,name='employeeupdate'),
   path('delete/<int:id>/',views.employeeDelete,name='employeedelete'),
]