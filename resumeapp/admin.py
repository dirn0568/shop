from django.contrib import admin

# Register your models here.
from resumeapp.models import User_Resume, User_Resume_Certificate, Resume_Title, Resume_ElementarySchool, \
    Resume_MiddleSchool, Resume_HighSchool, Resume_UniversitySchool, Resume_UniversitySchool_Major, \
    Resume_Career_Ability, Resume_Career, Resume_Career_Project

admin.site.register(User_Resume)
admin.site.register(User_Resume_Certificate)

admin.site.register(Resume_Title)
admin.site.register(Resume_ElementarySchool)
admin.site.register(Resume_MiddleSchool)
admin.site.register(Resume_HighSchool)
admin.site.register(Resume_UniversitySchool)

admin.site.register(Resume_UniversitySchool_Major)


admin.site.register(Resume_Career)
admin.site.register(Resume_Career_Ability)

admin.site.register(Resume_Career_Project)

