from django.shortcuts import render,redirect, get_object_or_404
from .forms import BoardWriteForm
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
import os
from config import settings
from django.utils import timezone
from django.http import HttpResponse


def main(request):
    topics = Board.objects.all() 
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
        board.image = request.POST['image']
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

def boardpaging(request) : #board 간략하게 paging
    now_page = request.GET.get('page',1)
    datas = Board.objects.order_by('-board_id')

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
    return render(request, 'board/board.html', context)
    

@csrf_exempt
def notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    context = {
        'notice': notice,
    }
    return render(request, 'board/notice_detail.html', context)


def download(request):
    id = request.GET.get('board_id')
    uploadFile = Board.objects.get(id=id)
    filepath = str(settings.BASE_DIR) + ('/media/%s' % uploadFile.image.name)
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
        return response


def comment(request, id):
    board = get_object_or_404(Board, pk=id)
    board.comment_set.create(
        content=request.POST.get('content'), create_date=timezone.now())
    comment = Answer(
        question=question, content=request.POST.get('content'),
        create_date=timezone.now())
        comment.save()
    return redirect('board:bord_detail', id=id)






   
