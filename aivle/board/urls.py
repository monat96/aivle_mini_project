from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('main/', views.main, name='main'),
    path('board/', views.boardpaging, name='board'),
    path('new/',views.new_topic,name='new_topic'),
]