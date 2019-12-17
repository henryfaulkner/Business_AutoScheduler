from django.shortcuts import render
from django.http import HttpResponse

def validate_email(email: str) -> bool:
    return re.match(
        '^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*'
        '@'
        '(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$',
        email) is not None

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the AutoScheduler index.")
