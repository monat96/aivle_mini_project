from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import BoardWriteForm
from aivle import board
from .models import *
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

def home(request):
    topics = board.objects.all()   #models의 Topic 개체 생성
    return render(request,'main.html',{'topics':topics})


@csrf_exempt
def register(request): #폼 이용한거 
    if request.method == 'POST':
        form = BoardWriteForm(request.POST)
        if form.is_valid():
            form.save()
            
            return render(request, 'list')
    else:
        form = BoardWriteForm()
    
    context = {'form' : form}
    return render(request, 'board/board_write.html', context)





def board_write(request): #폼 이용 안한거
    login_session = request.session.get('login_session', '')
    context = {'login_session': login_session}

    topics = board.objects.all()
    
    if request.method =='POST':
        title = request.POST['title']
        content = request.POST['content']

        author = User.objects.first()

        topic = board.objects.create(
            title = title,
            content = content,
            user_id = author,
        )

        
        return redirect('board_list')
    
    return render(request,'board_write.html', {'topics':topics})


   