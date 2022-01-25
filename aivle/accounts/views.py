from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib.auth import authenticate, login

# Create your views here.
@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        [print(i) for i in form]
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            form.save()
            return render(request, 'login/login.html')
    else:
        form = RegisterForm()
    
    context = {
        'form' : form
    }
    return render(request, 'register/register.html', context)



# Create your views here.


@login_required
def update(request):
    if request.method == "POST": #Post -> 수정한 내용 업데이트, Get -> 기존 데이터 instance 담아서 폼을 html넘김
        form = UserChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('upadate/update_complete.html', request.user)
        return render(
            request, 
            'update/update.html', 
            {'form': form }
            )

@login_required
def delete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('posts:list')
    return render(request, 'delete/delete.html')

