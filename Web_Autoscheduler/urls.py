from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('manager_log_reg/', views.manager_log_reg, name='manager_log_reg'),
]
