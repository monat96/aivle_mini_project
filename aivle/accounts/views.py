from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib.auth import authenticate, login


# Create your views here.
@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:login")
    else:
        form = RegisterForm()
    
    context = {'form' : form}
    return render(request, 'register.html', context)


@csrf_exempt
@login_required
def change_password(request):
  if request.method == "POST":
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
      user = form.save()
      update_session_auth_hash(request, user)
      messages.success(request, '비밀번호가 변경되었습니다.')
      return redirect('main')
    else:
      messages.error(request,'비밀번호를 확인해주세요.')
  else:
    form = PasswordChangeForm(request.user)
  return render(request, 'update/change_password.html',{'form':form})

@csrf_exempt
@login_required
def delete(request):
    if request.method == 'POST':
        request.user.delete()
        messages.success(request, '그 동안 이용해주셔서 감사합니다.')
        return redirect('main')
    return render(request, 'delete/delete.html')



