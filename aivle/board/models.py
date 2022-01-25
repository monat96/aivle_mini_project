from django.db import models
from django.db.models.fields import CharField, IntegerField, DateTimeField, FloatField
from django.utils.timezone import now
from django.conf import settings



class Board(models.Model):
    board_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name = "brduser_id")
    title = models.CharField(max_length= 45)
    content = models.CharField(max_length= 400)
    date = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField()
    dislike = models.IntegerField()
    hit_cnt = models.IntegerField()


    # def __str__(self):
    #     return self.title
    # # 제목이 board object가 되는 함수

    class Meta:
        db_table = 'board'




class Comment(models.Model):
    comment_num = models.IntegerField(primary_key=True)
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE, verbose_name = "cmtboard_id")
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name = "cmtuser_id")
    content = models.CharField(max_length= 45)
    like = models.IntegerField()
    dislike = models.IntegerField()

    class Meta:
        db_table = 'comment'

class File(models.Model):
    file_idx = models.IntegerField()
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name = "fleuser_id")
    stored_file_name = models.CharField(max_length=45)
    file_size = models.IntegerField()
    create_date = models.DateTimeField(default=now, editable=False)

    class Meta:
        db_table = 'file'

