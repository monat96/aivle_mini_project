from django.db import models
from django.utils.timezone import now
from django.conf import settings


class Board(models.Model):
    board_id = models.AutoField(primary_key=True, null=False)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name = "brduser_id", null=False)
    title = models.CharField(max_length=256, null=False)
    content = models.TextField(null=False)
    date = models.DateTimeField(default=now, editable=False, null=False)
    like = models.IntegerField(default=0, null=False)
    dislike = models.IntegerField(default=0, null=False)
    hit_cnt = models.IntegerField(default=0, null=False)

    class Meta:
        db_table = 'board'




class Comment(models.Model):
    comment_num = models.AutoField(primary_key=True)
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE, verbose_name = "cmtboard_id")
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name = "cmtuser_id")
    content = models.TextField()
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    class Meta:
        db_table = 'comment'

class File(models.Model):
    file_idx = models.AutoField(primary_key=True)
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name = "fleuser_id")
    stored_file_name = models.CharField(max_length=45)
    file_size = models.IntegerField()
    create_date = models.DateTimeField(default=now, editable=False)

    class Meta:
        db_table = 'file'

