from django.db import models

# Create your models here.
from accountapp.models import MyUser

class FriendRequestModel(models.Model):
    A_User = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='A_User')
    B_User = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='B_User')