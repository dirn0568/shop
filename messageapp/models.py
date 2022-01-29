from django.db import models

from accountapp.models import MyUser


class Message_Resume_Model(models.Model):
    message_resume_receive = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='message_resume_receive')

    message_resume_send = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='message_resume_send')

    message_detail = models.CharField(max_length=2000)

    message_date = models.DateField(auto_now=True)
    message_Time = models.TimeField(auto_now=True)

class Test_Data(models.Model):
    test = models.CharField(max_length=2000)