from django.shortcuts import render, redirect, get_object_or_404
from .forms import BoardWriteForm, CommentForm
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
import os
from config import settings
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
# from django.core import serializers
# from django.core.serializers.json import DjangoJSONEncoder
# from django.http import HttpResponse
# import json


def main(request):
    topics = Board.objects.all() 
    return render(request,'board/main.html',{'topics':topics})


def mypage(request):
    now_page = request.GET.get('page', 1)
    user = request.user
    datas = Board.objects.filter(user_id = user).order_by('-id')

    paginator = Paginator(datas, 10)
    info = paginator.get_page(now_page)
    start_page = (int(now_page)-1) // 10 * 10 + 1
    end_page = start_page + 1

    if end_page > paginator.num_pages:
        end_page = paginator.num_pages

    context = {
        'info': info,
        'page_range': range(start_page, end_page + 1)
    }
    return render(request, 'board/mypage.html', context)


@csrf_exempt
@login_required
def withdraw(request):
    if request.method == 'POST':
        password = request.POST.get('password', '')
        user = request.user
        if check_password(password, user.password):
            user.delete()
            messages.success(request, '그 동안 이용해주셔서 감사합니다.')
            return redirect('board:main')

    return render(request, 'board/withdraw.html')


@csrf_exempt

def board_write(request):
    if request.method == 'POST':
        form = BoardWriteForm(request.POST)
        if form.is_valid():
            writing = form.save(commit=False)
            writing.user = request.user
            writing.save()
            return redirect('board:board')
    else:
        form = BoardWriteForm()

    context = {'form': form}
    return render(request, 'board/write.html', context)


@csrf_exempt
def board_detail(request, pk):
    board = get_object_or_404(Board, pk=pk)
    context = {
        'board': board,
    }
    board.hit_cnt += 1
    board.save()

    return render(request, 'board/detail.html', context)



@csrf_exempt
def boardedit(request, pk):
    board = Board.objects.get(board_id=pk)
    if request.method == "POST":
        board.title = request.POST['title']
        board.content = request.POST['content']
        board.image = request.FILES['image']
        board.save()
        return redirect('board_list')
    else:
        boardForm = BoardWriteForm
        return render(request, 'board/update.html', {'boardForm': boardForm})


@csrf_exempt
def boarddelete(request, pk):
    board = Board.objects.get(board_id=pk)
    board.delete()
    return redirect('board_list')


@csrf_exempt
def boardpaging(request) : #board 간략하게 paging
    now_page = request.GET.get('page',1)
    datas = Board.objects.order_by('-id')

    p = Paginator(datas, 10)
    info = p.get_page(now_page)
    start_page = (int(now_page) - 1) // 10 * 10 + 1
    end_page = start_page + 9
    if end_page > p.num_pages:
        end_page = p.num_pages
    context = {
        'info': info,
        'page_range': range(start_page, end_page + 1)
    }
    return render(request, 'board/board.html', context)

    
@csrf_exempt    
def notice_boardpaging(request):
    now_page = request.GET.get('page',1)
    datas =  Notice.objects.order_by('-id')

    p = Paginator(datas,10)
    info = p.get_page(now_page)
    start_page = (int(now_page) - 1) // 10 * 10 + 1
    end_page = start_page + 9
    if end_page > p.num_pages:
        end_page = p.num_pages
    context = {
        'info' : info,
        'page_range' : range(start_page, end_page + 1)
    }
    return render(request, 'board/notice.html', context) #notice.html => board에서 공지사항이라고만 수정하고 글쓰기 버튼 없앤 거 

@csrf_exempt
def notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    context = {
        'notice': notice,
    }
    notice.hit_cnt += 1
    notice.save()

    return render(request, 'board/notice_detail.html', context)


@csrf_exempt
def download(request):
    id = request.GET.get('id')
    uploadFile = Board.objects.get(id=id)
    filepath = str(settings.BASE_DIR) + ('/media/%s' % uploadFile.image.name)
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
        return response


@csrf_exempt
def comment(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.board = board
            comment.save()
            return redirect('board:board_detail', board_id=board_id)
    else:
        form = CommentForm()

    context = {'board': board, 'form': form}
    return render(request, 'board:board_detail', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('board:mypage')
    else:
        form = PasswordChangeForm(request.user)

    context = {
        'form': form,
    }

    return render(request, 'board/change_password.html', context)
