from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('main/', views.main, name='main'),
    path('board/', views.board, name='board'),
    path('init_board/', views.init_board, name='init_board'),
]