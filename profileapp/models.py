from django.db import models

# Create your models here.
from accountapp.models import MyUser


class User_Profile(models.Model):
    profile = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='profile')

    profile_text = models.TextField(max_length=1000, null=True, blank=True)
    profile_img = models.ImageField(upload_to='Profile_img/', null=True, blank=True)