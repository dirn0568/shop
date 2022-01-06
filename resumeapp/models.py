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

    resume_date = models.DateField(auto_now=True)
    resume_Time = models.TimeField(auto_now=True)

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

class Resume_Out_Play(models.Model):
    resume_out_play = models.ForeignKey(Resume_Title, on_delete=models.CASCADE, related_name='resume_out_play')

    resume_out_activity = models.CharField(max_length=500)
    resume_out_place = models.CharField(max_length=500)
    resume_out_start_play = models.CharField(max_length=500)
    resume_out_end_play = models.CharField(max_length=500)
    resume_out_play_text = models.CharField(max_length=500)
class Resume_Prize_Play(models.Model):
    resume_prize_play = models.ForeignKey(Resume_Title, on_delete=models.CASCADE, related_name='resume_prize_play')

    resume_prize_certificate = models.CharField(max_length=500)
    resume_prize_place = models.CharField(max_length=500)
    resume_prize_title = models.CharField(max_length=500)
    resume_prize_date = models.CharField(max_length=500)

class Resume_Port_Polio(models.Model):
    resume_port_polio = models.ForeignKey(Resume_Title, on_delete=models.CASCADE, related_name='resume_port_polio')

    resume_port_polio_detail = models.FileField()
class Resume_Self_Introduce(models.Model):
    resume_self_introduce = models.ForeignKey(Resume_Title, on_delete=models.CASCADE, related_name='resume_self_introduce')

    resume_self_introduce_title = models.CharField(max_length=500)
    resume_self_introduce_text = models.CharField(max_length=3000)


##########################################################################################################

# 경력

class Resume_Career(models.Model):
    resume_career = models.ForeignKey(Resume_Title, on_delete=models.CASCADE, related_name='resume_career')

    resume_company_name = models.CharField(max_length=50)
    resume_career_start_time = models.CharField(max_length=200)
    resume_career_end_time = models.CharField(max_length=200)
    resume_career_out = models.CharField(max_length=200)
    resume_career_position = models.CharField(max_length=200)
    resume_career_position_detail = models.CharField(max_length=200)
    resume_career_money = models.CharField(max_length=20000)
    resume_career_money_detail = models.CharField(max_length=200)
    resume_career_position_detail2 = models.CharField(max_length=200)

class Resume_Career_Ability(models.Model):
    resume_career_ability = models.ForeignKey(Resume_Title, on_delete=models.CASCADE, related_name='resume_career_ability')

    resume_career_ability_text = models.CharField(max_length=2000)

class Resume_Career_Project(models.Model):
    resume_career_project = models.ForeignKey(Resume_Title, on_delete=models.CASCADE, related_name='resume_career_project')

    resume_career_project_text = models.CharField(max_length=2000)
    resume_career_project_start_time = models.CharField(max_length=200)
    resume_career_project_end_time = models.CharField(max_length=200)
    resume_career_project_text_detail = models.CharField(max_length=2000)

###################################################################################################################################
# resume5

class Resume_Hope_Work(models.Model):
    resume_hope_work = models.ForeignKey(Resume_Title, on_delete=models.CASCADE, related_name='resume_hope_work')

    resume_hope_work_start_time = models.CharField(max_length=200)
    resume_hope_work_end_time = models.CharField(max_length=200)
    resume_hope_work_money = models.CharField(max_length=200)

class Resume_Hope_Work_Field(models.Model):
    resume_hope_work_field = models.ForeignKey(Resume_Title, on_delete=models.CASCADE, related_name='resume_hope_work_field')

    resume_hope_work_field1 = models.CharField(max_length=200)


class Resume_Hope_Work_Work(models.Model):
    resume_hope_work_work = models.ForeignKey(Resume_Title, on_delete=models.CASCADE, related_name='resume_hope_work_work')

    resume_hope_work_work1 = models.CharField(max_length=200)