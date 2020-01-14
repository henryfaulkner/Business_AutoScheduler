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
    registered = 'registerButton' in request.POST # TRUE if registering
    logged_in = 'loginButton' in request.POST # TRUE if logging in
    if registered is TRUE:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST) 
            if form.is_valid(): 
                form.save() 
                username = form.cleaned_data.get('username') 
                email = form.cleaned_data.get('email') 
                ######################### mail system ####################################  
                htmly = get_template('user / confirm_email_reg.html') 
                d = { 'username': username } 
                subject, from_email, to = 'welcome', 'autoscheduler156@gmail.com', email 
                html_content = htmly.render(d) 
                msg = EmailMultiAlternatives(subject, html_content, from_email, [to]) 
                msg.attach_alternative(html_content, "text / html") 
                msg.send() 
                ##################################################################  
                messages.success(request, f'Your account has been created ! You are now able to log in') 
                return redirect('login') 
        else: 
            form = UserRegisterForm()
    if logged_in is TRUE:
        if request.method == 'POST': 
            # AuthenticationForm_can_also_be_used__ 
            username = request.POST['username'] 
            password = request.POST['password'] 
            user = authenticate(request, username = username, password = password) 
            if user is not None: 
                form = login(request, user) 
                messages.success(request, f' wecome {username} !!') 
                return redirect('index') 
            else: 
                messages.info(request, f'account done not exit plz sign in') 
        
    return render(request, 'Web_Autoscheduler/manager_log_reg.html')

def employee_log_reg(request):
    return render(request, 'Web_Autoscheduler/employee_log_reg.html')

def confirm_email_reg(request):
    return render(request, 'Web_Autoscheduler/confirm_email_reg.html')
