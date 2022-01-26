from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('main/', views.main, name='main'),
    #path('board/', views.board, name='board'),
    path('board/', views.boardpaging, name='board'),
    # path('new/',views.new_topic,name='new_topic'),
    path('write/',views.board_write, name = 'write'), # 게시글 작성
    path('mypage/', views.mypage, name='mypage'),
    # path('detail/<int:pk>/',views.boarddetail, name = 'board_detail'),
    # path('detail/<int:pk>/edit', views.boardedit, name = 'board_edit'),
    # path('detail/<int:pk>/delete',views.boarddelete,name='board_delete'),
    # path('notice',views.notice_detail, name = 'noticedetail'),
    # path('detail/<int:pk>/commentwrite',views.comment_write, name = 'comment_write'),
]