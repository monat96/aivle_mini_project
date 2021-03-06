from django.db import models
from django.utils.timezone import now
from django.conf import settings
from django.contrib.auth.models import User


class Board(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, null=False)
    content = models.TextField(null=False)
    image = models.FileField(null = True, blank = True, upload_to='img/')
    date = models.DateTimeField(default=now, editable=False, null=False)
    # like = models.IntegerField(default=0, null=False)
    # dislike = models.IntegerField(default=0, null=False)
    hit_cnt = models.IntegerField(default=0, null=False)

    # def __str__(self):
    #     return self.title
    # # 제목이 board object가 되는 함수
    class Meta:
        db_table = 'board'




class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=now, editable=False, null=False)
    content = models.TextField()
    # like = models.IntegerField(default=0)
    # dislike = models.IntegerField(default=0)

    class Meta:
        db_table = 'comment'

# class File(models.Model):
#     file_idx = models.AutoField(primary_key=True)
#     board_id = models.ForeignKey(Board, on_delete=models.CASCADE)
#     user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name = "fleuser_id")
#     stored_file_name = models.CharField(max_length=45)
#     file_size = models.IntegerField()
#     create_date = models.DateTimeField(default=now, editable=False)

#     class Meta:
#         db_table = 'file'

class Notice(models.Model):
    title = models.CharField(max_length= 45)
    content = models.CharField(max_length= 400)
    date = models.DateTimeField(default=now, editable=False, null=False)
    username= models.CharField(max_length= 45, default="관리자")
    class Meta:
        db_table = 'notice'
