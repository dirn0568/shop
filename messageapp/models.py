from django.db import models

from accountapp.models import MyUser


# class Message_Receive_Model(models.Model):
#     message_receive_receive = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='message_receive_receive')
#
#     message_receive_send = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='message_receive_send')
#
#     message_receive_title = models.CharField(max_length=2000)
#     message_receive_detail = models.CharField(max_length=2000)
#
#     message_receive_date = models.DateField(auto_now=True)
#     message_receive_Time = models.TimeField(auto_now=True)
#     message_receive_date_time = models.DateTimeField(auto_now=True)
#
#     message_receive_file = models.FileField(upload_to='message/', null=True, blank=True)

class Message_Send_Model(models.Model):
    message_send_receive = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='message_send_receive')

    message_send_send = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='message_send_send')

    message_send_title = models.CharField(max_length=2000)
    message_send_detail = models.TextField()

    message_send_date = models.DateField(auto_now=True)
    message_send_Time = models.TimeField(auto_now=True)
    message_send_date_time = models.DateTimeField(auto_now=True)

    message_send_file = models.FileField(upload_to='message/', null=True, blank=True)

class Message_Resume_Model(models.Model):
    message_resume_receive = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='message_resume_receive')

    message_resume_send = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='message_resume_send')

    message_title = models.CharField(max_length=2000)
    message_detail = models.CharField(max_length=2000)

    message_date = models.DateField(auto_now=True)
    message_Time = models.TimeField(auto_now=True)
    message_date_time = models.DateTimeField(auto_now=True)

    message_file = models.FileField(upload_to='message/', null=True, blank=True)

class Message_Propose_Model(models.Model):
    message_propose_receive = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='message_propose_receive')

    message_propose_send = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='message_propose_send')

    message_propose_detail = models.TextField()

    message_propose_company_group = models.CharField(max_length=200)
    message_propose_company_name = models.CharField(max_length=200)
    message_propose_company_ceo = models.CharField(max_length=100)
    message_propose_company_logo = models.FileField(upload_to='message/', null=True, blank=True)
    message_propose_company_phone_number = models.CharField(max_length=2000)

    message_propose_date = models.DateField(auto_now=True)
    message_propose_Time = models.TimeField(auto_now=True)
    message_propose_date_time = models.DateTimeField(auto_now=True)

class Test_Data(models.Model):
    test = models.CharField(max_length=2000)