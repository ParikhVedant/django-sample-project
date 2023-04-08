from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("Hello World!")

def home2(request):
    return render(request, 'home.html')

def current_time(request):
    now = datetime.now()
    time_str = now.strftime("%d/%m/%Y %H:%M:%S")

    return render(request, 'home2.html', {"time": time_str})

def home3_get(request):

    form_data = request.GET
    employee_email = form_data.get('email')
    employee_password = form_data.get('password')
    
    return render(request, 'home2.html', {"time": employee_email})

def addition(request):

    return render(request, 'addition.html')

def addition_result(request):

    form_data = request.GET
    a = int(form_data.get('a'))
    b = int(form_data.get('b'))
    c = a + b
    
    return render(request, 'addition_result.html', {
        "a": a,
        "b": b,
        "c": c,
    })