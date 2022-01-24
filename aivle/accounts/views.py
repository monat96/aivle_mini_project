from django.shortcuts import render, redirect

# Create your views here.
def login(request):
    return render(request, 'login/login.html')
def register(request):
    return render(request, 'register/register.html')