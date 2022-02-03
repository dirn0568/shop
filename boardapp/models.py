from django.db import models

# Create your models here.
from accountapp.models import MyUser


class Board_Model(models.Model):
    board_user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='board_user')

    board_title = models.CharField(max_length=2000)
    board_detail = models.TextField()

    board_date_time = models.DateTimeField(auto_now=True)

    board_file = models.FileField(upload_to='board/', null=True, blank=True)

class Board_Gonge_Model(models.Model):
    board_gonge_user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='board_gonge_user')

    board_gonge_title = models.CharField(max_length=2000)
    board_gonge_detail = models.TextField()

    board_gonge_date_time = models.DateTimeField(auto_now=True)

    board_gonge_file = models.FileField(upload_to='board/', null=True, blank=True)

class Board_Jaro_Model(models.Model):
    board_jaro_user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='board_jaro_user')

    board_jaro_title = models.CharField(max_length=2000)
    board_jaro_detail = models.TextField()

    board_jaro_date_time = models.DateTimeField(auto_now=True)

    board_jaro_file = models.FileField(upload_to='board/', null=True, blank=True)
