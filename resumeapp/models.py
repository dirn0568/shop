from django.db import models

# Create your models here.
from accountapp.models import MyUser


class User_Resume(models.Model):
    resume = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='resume')

    resume_title = models.CharField(max_length=100)

    resume_school = models.TextField(max_length=1000, null=True, blank=True)
    resume_career = models.TextField(max_length=1000, null=True, blank=True)
    resume_certificate = models.FileField(upload_to='resume_file/', null=True, blank=True)

    resume_text = models.TextField(max_length=10000, null=True, blank=True)