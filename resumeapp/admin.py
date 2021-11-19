from django.contrib import admin

# Register your models here.
from resumeapp.models import User_Resume, User_Resume_Certificate, Resume_Title, Resume_ElementarySchool

admin.site.register(User_Resume)
admin.site.register(User_Resume_Certificate)

admin.site.register(Resume_Title)
admin.site.register(Resume_ElementarySchool)