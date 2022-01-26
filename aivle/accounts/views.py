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
def change_password(request):
  if request.method == "POST":
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
      user = form.save()
      update_session_auth_hash(request, user)
      messages.success(request, '비밀번호가 변경되었습니다.')
      return redirect('board/main.html')
    else:
      messages.error(request,'비밀번호를 확인해주세요.')
  else:
    form = PasswordChangeForm(request.user)
  return render(request, 'update/change_password.html',{'form':form})


def detail(request, pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=pk)
    context = {
        'user': user
    }
    return render(request, 'accounts/detail.html', context)

