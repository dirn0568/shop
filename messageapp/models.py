from django.db import models

from accountapp.models import MyUser


class Message_Model(models.Model):
    message_model = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='message_model')

    message_detail = models.CharField(max_length=2000)

    message_date = models.DateField(auto_now=True)
    message_Time = models.TimeField(auto_now=True)