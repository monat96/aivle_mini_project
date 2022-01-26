from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'board'
urlpatterns = [
    path('main/', views.main, name='main'),
    path('board/', views.boardpaging, name='board'),
    path('write/',views.board_write, name = 'write'), # 게시글 작성
    # path('detail/<int:pk>/',views.boarddetail, name = 'board_detail'),
    # path('detail/<int:pk>/edit', views.boardedit, name = 'board_edit'),
    # path('detail/<int:pk>/delete',views.boarddelete,name='board_delete'),
    # path('notice',views.notice_detail, name = 'noticedetail'),
    # path('detail/<int:pk>/commentwrite',views.comment_write, name = 'comment_write'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)