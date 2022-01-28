from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('', views.main, name='main'),
    path('board/', views.boardpaging, name='board'),
    path('notice/', views.notice_boardpaging, name='notice'),
    path('write/',views.board_write, name = 'write'), # 게시글 작성
    path('detail/<int:pk>/',views.board_detail, name = 'board_detail'),
    path('download/', views.download, name='download'),
    # path('detail/<int:pk>', views.comment, name='comment'),
    path('mypage/', views.mypage, name='mypage'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('change_password/', views.change_password, name='change_password'),
    path('detail/<int:pk>/download',views.download, name="download"),
    # path('detail/<int:pk>/',views.boarddetail, name = 'board_detail'),
    # path('detail/<int:pk>/edit', views.boardedit, name = 'board_edit'),
    # path('detail/<int:pk>/delete',views.boarddelete,name='board_delete'),
    path('notice_detail/<int:pk>/',views.notice_detail, name = 'notice_detail'),
    # path('detail/<int:pk>/commentwrite',views.comment_write, name = 'comment_write'),
]