from django.forms import ModelForm
from django import forms

from resumeapp.models import User_Resume

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