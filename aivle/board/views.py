from django.shortcuts import render,redirect, get_object_or_404
from .forms import BoardWriteForm
from aivle import board
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
import json

def main(request):
    topics = board.objects.all() 
    return render(request,'main.html',{'topics':topics})


@csrf_exempt
def board_write(request):
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
def board_detail(request, pk):
    board = get_object_or_404(Board, pk=pk)
    context = {
        'board':board,
    }
    return render(request, 'board/detail.html', context)

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


@csrf_exempt
def notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    context = {
        'notice': notice,
    }
    return render(request, 'board/notice_detail.html', context)


def comment_write(request, pk):
    post = get_object_or_404(Board, id=pk)
    user_id = request.POST.get('user_id')
    content = request.POST.get('content')
    if content:
        comment = Comment.objects.create(post=post, content=content, user_id=request.user)
        post.save()
        data = {
            'user_id': user_id,
            'content': content,
        }
        if request.user == post.user_id:
            data['self_comment'] = '(글쓴이)'
        
        return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type = "application/json")








   