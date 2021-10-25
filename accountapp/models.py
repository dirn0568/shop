from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class MyUser(AbstractUser):
    nickname = models.CharField(max_length=20, unique=True)

class Friend_List(models.Model):
    friend = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='friend')
    friend_relation = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='friend_relation')

    class Meta:
        unique_together = ('friend', 'friend_relation')