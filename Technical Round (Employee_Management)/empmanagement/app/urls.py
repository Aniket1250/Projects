from django.urls import path
from app import views
urlpatterns = [
    path('',views.home),

    path('deptlist',views.deptlist,name='deptlist'),
    path('deptform',views.add_department),
    path('deptview/<int:pk>',views.department_detail),
    path('deptedit/<int:pk>', views.edit_department, name='edit_department'),
    path('department/delete/<int:department_id>/', views.delete_department, name='delete_department'),
    path('department/<int:department_id>/hierarchy/', views.department_hierarchy, name='department_hierarchy'),

    path('emplist',views.emplist,name='emplist'),  
    path('empform',views.add_employee), 
    path('empview/<int:pk>/',views.employee_detail, name='employee_detail'),
    path('employee/edit/<int:employee_id>/', views.edit_employee, name='edit_employee'),
    path('employee/delete/<int:employee_id>/', views.delete_employee, name='delete_employee'),

    path('salaries/', views.salary_list, name='salary_list'),
    path('salary/<int:entry_id>/',views.salary_detail, name='salary_detail'),
    path('salary/add/', views.add_salary_entry, name='add_salary_entry'),
    path('salary/edit/<int:entry_id>/', views.edit_salary_entry, name='edit_salary_entry'),
    path('salary/report/', views.salary_report, name='salary_report'),


]
