from django.shortcuts import render, redirect
from .forms import WritingForm

# Create your views here.
def main(request):
    return render(request, 'board/main.html')
def board(request):
    return render(request, 'board/board.html')
def init_board(request):
    if request.method == 'POST':
        form = WritingForm(request.POST)
        if form.is_valid():
            writing = form.save(commit=False)
            writing.user_id = request.user
            writing.save()
            return redirect('board:board')
    else:
        form = WritingForm()
    context = {'form':form}
    return render(request, 'board/init_board.html', context)