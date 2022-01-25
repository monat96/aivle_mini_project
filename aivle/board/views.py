from django.shortcuts import render,redirect
from .forms import BoardWriteForm
from aivle import board
from .models import *
from django.views.decorators.csrf import csrf_exempt

def home(request):
    topics = board.objects.all()   #models의 Topic 개체 생성
    return render(request,'main.html',{'topics':topics})


@csrf_exempt
def board_write(request): #폼 이용한거 
    if request.method == 'POST':
        form = BoardWriteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_list')
    else:
        form = BoardWriteForm()
    
    context = {'form' : form}
    return render(request, 'board/board_write.html', context)

@csrf_exempt
def boardedit(request, pk):
    board = Board.objects.get(id=pk)
    if request.method == "POST":
        board.title = request.POST['title']
        board.content = request.POST['content']
        board.user_id = request.POST['user_id']
        board.save()
        return redirect('board_list')
    else:
        boardForm = BoardWriteForm
        return render(request, 'board/update.html', {'boardForm':boardForm})

@csrf_exempt
def boarddelete(request, pk):
    board = Board.objects.get(id=pk)
    board.delete()
    return redirect('board_list')

   