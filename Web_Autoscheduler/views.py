from django.shortcuts import render
from django.http import HttpResponse
from django.template import engines
from django.template import loader

def validate_email(email: str) -> bool:
    return re.match(
        '^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*'
        '@'
        '(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$',
        email) is not None

TEMPLATES = [{'BACKEND': 'django.template.backends.django.DjangoTemplates'},]

# Create your views here.
def index(request):
    return render(request, 'Web_Autoscheduler/index.html')

def manager_log_reg(request):
    return render(request, 'Web_Autoscheduler/manager_log_reg.html')


