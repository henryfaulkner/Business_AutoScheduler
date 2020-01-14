from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('manager_log_reg/', views.manager_log_reg, name='manager_log_reg'),
    path('employee_log_reg/', views.employee_log_reg, name='employee_log_reg'),
    # separate 'manager_log_reg/confirm_email_registered' & 'employee_log_reg/confirm_email_registered' in future
    path('confirm_email_reg/', views.confirm_email_reg, name='confirm_email_reg')
]
