from django.shortcuts import render, redirect
from .forms import CustomUserForm, UserChangeForm
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# Create your views here.

@csrf_exempt
def register(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect('accounts:login')
    else:
        form = CustomUserForm()
    return render(request, 'register/register.html', {'form' : form })


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




       
>>>>>>> 김란희
