from django.shortcuts import render
from django.http import HttpResponse
from django.template import engines
from django.template.loader import render_to_string

TEMPLATES = [{'BACKEND': 'django.template.backends.django.DjangoTemplates'},]

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the AutoScheduler index.")

def login(request):
    html = '''<!DOCTYPE html>
    <html lang='en'>
        <head>
            <title>Login Page</title>
        </head>
        <body>
            <form>
                <p>email</p>
                <input type="text"><br>
                <p>password</p>
                <input type="text" style="display:hidden"><br>
            </form>
        </body>
    </html>'''

    return HttpResponse(html)


