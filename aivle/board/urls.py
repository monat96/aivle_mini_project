from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('main/', views.main, name='main'),
<<<<<<< HEAD
    path('board/', views.boardpaging, name='board'),
    path('new/',views.new_topic,name='new_topic'),
=======
    path('boardwrite/',views.board_write, name = 'board_write'),
    path('detail/<int:pk>/',views.boarddetail, name = 'board_detail'),
    path('detail/<int:pk>/edit', views.boardedit, name = 'board_edit'),
    path('detail/<int:pk>/delete',views.boarddelete,name='board_delete'),
    path('notice',views.notice_detail, name = 'noticedetail'),
>>>>>>> 597a79558ab3458503a52df0621e8544cc6e6ed6
]