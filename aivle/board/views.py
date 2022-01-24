from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'board/main.html')
def board(request):
    return render(request, 'board/board.html')