from django.db import models

# Create your models here.
from accountapp.models import MyUser


class Report_Data(models.Model):
    report_send_user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='report_send_user')
    report_receive_user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='report_receive_user')

    report_title = models.CharField(max_length=200, null=True, blank=True)
    report_detail = models.CharField(max_length=2000, null=True, blank=True)