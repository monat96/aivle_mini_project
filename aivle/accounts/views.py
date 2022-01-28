from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import get_user_model

# Create your views here.
@csrf_exempt
def register(request):
    if request.user.is_authenticated:
      return redirect('board:main')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:login")
    else:
        form = RegisterForm()
    
    context = {'form' : form}
    return render(request, 'register.html', context)
