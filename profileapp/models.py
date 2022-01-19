from django.db import models

# Create your models here.
from accountapp.models import MyUser


class User_Profile(models.Model):
    profile = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='profile')

    user_name = models.CharField(max_length=100)
    user_birthday = models.CharField(max_length=100)
    user_gender = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    user_email = models.CharField(max_length=100)
    user_page = models.CharField(max_length=100)

    profile_text = models.TextField(max_length=1000, null=True, blank=True)
    profile_img = models.ImageField(upload_to='Profile_img/', null=True, blank=True)

    user_open = models.IntegerField(default=1)