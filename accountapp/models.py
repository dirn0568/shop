from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class MyUser(AbstractUser):
    nickname = models.CharField(max_length=20, unique=True)

    company_group = models.CharField(max_length=100)
    company_number = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    company_ceo = models.CharField(max_length=100)

    company_logo = models.FileField(upload_to='company_logo/', null=True, blank=True)
    company_phone_number = models.CharField(max_length=100)

    company_paper = models.FileField(upload_to='company_paper/', null=True, blank=True)

    sos_report = models.IntegerField(default=0)

class Friend_List(models.Model):
    friend = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='friend')
    friend_relation = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='friend_relation')

    class Meta:
        unique_together = ('friend', 'friend_relation')