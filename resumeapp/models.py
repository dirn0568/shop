from django.db import models

# Create your models here.
from accountapp.models import MyUser

##################################################################################################################

# 테스트 버전 1

class User_Resume(models.Model):
    resume = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='resume')

    resume_title = models.CharField(max_length=100)

    resume_school = models.TextField(max_length=1000, null=True, blank=True)
    resume_career = models.TextField(max_length=1000, null=True, blank=True)

    resume_text = models.TextField(max_length=10000, null=True, blank=True)

class User_Resume_Certificate(models.Model):
    certificate = models.ForeignKey(User_Resume, on_delete=models.CASCADE, related_name='certificate')

    resume_certificate = models.FileField(upload_to='resume_file/', null=True, blank=True)

##################################################################################################################

# 테스트 버전2

class Resume_Title(models.Model):
    resume_title = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='resume_title')

class Resume_ElementarySchool(models.Model):
    resume_elementary = models.ForeignKey(Resume_Title, on_delete=models.CASCADE, related_name='resume_elementary')

    elementary_school_name = models.CharField(max_length=50)
    # elementary_field_name = models.Choices('서울', '경기')
    elementary_start_time = models.DateField()
    elementary_end_time = models.DateField()