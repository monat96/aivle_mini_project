from django.db import models
from django.db.models.fields import CharField, IntegerField, DateTimeField, FloatField
from django.utils.timezone import now


# Create your models here.

class Board(models.Model):
    board_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey('accounts.CustomUser')
    title = models.CharField(max_length= 45)
    content = models.CharField(max_length= 400)
    date = models.DateTimeField(default=now, editable=False)
    like = models.IntegerField()
    dislike = models.IntegerField()
    hit_cnt = models.IntegerField()

    class Meta:
        db_table = 'board'




class Comment(models.Model):
    comment_num = models.IntegerField(primary_key=True)
    board_id = models.ForeignKey(Board, on_delete=models.SET_NULL)
    user_id = models.ForeignKey('accounts.CustomUser')
    nickname = models.ForeignKey('accounts.CustomUser')
    content = models.CharField(max_length= 45)
    like = models.IntegerField()
    dislike = models.IntegerField()

    class Meta:
        db_table = 'comment'

class File(models.Model):
    file_idx = models.IntegerField()
    board_id = models.ForeignKey(Board, on_delete=models.SET_NULL)
    user_id = models.ForeignKey('accounts.CustomUser')
    stored_file_name = models.CharField(max_length=45)
    file_size = models.IntegerField()
    create_date = models.DateTimeField(default=now, editable=False)

    class Meta:
        db_table = 'file'

