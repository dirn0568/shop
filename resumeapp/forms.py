
from django.forms import ModelForm, DateField
from django import forms

from pickme import settings
from resumeapp.models import User_Resume, Resume_ElementarySchool, Resume_MiddleSchool, Resume_HighSchool, \
    Resume_UniversitySchool, Resume_UniversitySchool_Major, Resume_Title, Resume_Career, Resume_Career_Ability, \
    Resume_Career_Project


###################################################################################################

# 테스트 버전 0

class ResumeForm(ModelForm):
    resume_title = forms.CharField(label='이력서 제목',
                                   widget=forms.TextInput(attrs={'autofocus': 'autofocus',
                                                                'autocomplete': 'off',
                                                                'size': '40',
                                                                'style': 'font-size: x-large',
                                                                }))
    resume_school = forms.CharField(label='학력',
                                    widget=forms.TextInput(attrs={'autofocus': 'autofocus',
                                                                'autocomplete': 'off',
                                                                'size': '40',
                                                                'style': 'font-size: x-large',
                                                                }))
    resume_career = forms.CharField(label='경력',
                                    widget=forms.TextInput(attrs={'autofocus': 'autofocus',
                                                                'autocomplete': 'off',
                                                                'size': '40',
                                                                'style': 'font-size: x-large',
                                                                }))
    resume_certificate = forms.FileField(label='자격증')
    resume_text = forms.TextInput()

    class Meta:
        model = User_Resume
        fields = ['resume_title', 'resume_school', 'resume_career', 'resume_certificate', 'resume_text']

class Update_ResumeForm(ResumeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

#############################################################################################################

# 테스트 버전 2

class ResumeTitleForm(ModelForm):
    class Meta:
        model = Resume_Title
        fields = []

class ResumeElementaryForm(ModelForm):
    # elementary_start_time = DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = Resume_ElementarySchool
        fields = []

class ResumeMiddleForm(ModelForm):
    # elementary_start_time = DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = Resume_MiddleSchool
        fields = []

class ResumeHighForm(ModelForm):
    # elementary_start_time = DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = Resume_HighSchool
        fields = []

class ResumeUniversityForm(ModelForm):
    # elementary_start_time = DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = Resume_UniversitySchool
        fields = []

class ResumeUniversitySchoolMajor_Form(ModelForm):
    class Meta:
        model = Resume_UniversitySchool_Major
        fields = []

##############################################################################################

class ResumeCareerForm(ModelForm):
    class Meta:
        model = Resume_Career
        fields = []

class ResumeCareerAbilityForm(ModelForm):
    class Meta:
        model = Resume_Career_Ability
        fields = []

class ResumeCareerProjectForm(ModelForm):
    class Meta:
        model = Resume_Career_Project
        fields = []

