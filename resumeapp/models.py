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

    resume_title_detail = models.CharField(max_length=2000)

class Resume_ElementarySchool(models.Model):
    resume_elementary = models.ForeignKey(Resume_Title, on_delete=models.CASCADE, related_name='resume_elementary')

    elementary_school_name = models.CharField(max_length=50)
    elementary_field_name = models.CharField(max_length=50)
    elementary_start_time = models.CharField(max_length=200)
    elementary_end_time = models.CharField(max_length=200)

class Resume_MiddleSchool(models.Model):
    resume_middle = models.ForeignKey(Resume_Title, on_delete=models.CASCADE, related_name='resume_middle')

    middle_school_name = models.CharField(max_length=50)
    middle_field_name = models.CharField(max_length=50)
    middle_start_time = models.CharField(max_length=200)
    middle_end_time = models.CharField(max_length=200)

class Resume_HighSchool(models.Model):
    resume_high = models.ForeignKey(Resume_Title, on_delete=models.CASCADE, related_name='resume_high')

    high_school_name = models.CharField(max_length=50)
    high_field_name = models.CharField(max_length=50) # 지역
    high_start_time = models.CharField(max_length=200)
    high_end_time = models.CharField(max_length=200)
    high_major = models.CharField(max_length=200) # 전공계열

class Resume_UniversitySchool(models.Model):
    resume_university = models.ForeignKey(Resume_Title, on_delete=models.CASCADE, related_name='resume_university')

    university_study_year = models.CharField(max_length=50)
    university_school_name = models.CharField(max_length=50)
    university_field_name = models.CharField(max_length=50)
    university_start_time = models.CharField(max_length=200)
    university_end_time = models.CharField(max_length=200)
    university_study_time = models.CharField(max_length=200)
    university_study_level = models.CharField(max_length=200)
    university_finaltest = models.CharField(max_length=2000)

class Resume_UniversitySchool_Major(models.Model):
    resume_university_major = models.ForeignKey(Resume_Title, on_delete=models.CASCADE, related_name='resume_university_major')

    resume_university_major_list = models.CharField(max_length=200)
    resume_university_major_detail = models.CharField(max_length=200)
