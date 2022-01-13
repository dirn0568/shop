
from django.http import request

# Create your views here.
from django.shortcuts import render

from accountapp.models import MyUser
from resumeapp.models import Resume_Title, Resume_Hope_Work_Field, Resume_Hope_Work_Work, Resume_ElementarySchool, \
    Resume_MiddleSchool, Resume_HighSchool, Resume_UniversitySchool, Resume_UniversitySchool_Major


def search_resume(request):
    context = {}

    if request.method == 'POST' and request.POST.get('resume_submit1'):
        print(request.POST)
        temp_resume = Resume_Title.objects.all()
        answer_list = []
        for resume_title in temp_resume:
            if resume_title.resume_open == 1:
                temp_field = Resume_Hope_Work_Field.objects.filter(resume_hope_work_field=resume_title)
                temp_work = Resume_Hope_Work_Work.objects.filter(resume_hope_work_work=resume_title)
                field_list = request.POST.getlist('accordion2')
                work_list = request.POST.getlist('work2')
                # field_list = request.POST.getlist('work2')
                # print(field_list)
                answer_field = 0
                answer_work = 0
                for resume_field in temp_field:
                    if field_list.count(resume_field.resume_hope_work_field1) >= 1:
                        answer_field += 1
                for resume_work in temp_work:
                    if work_list.count(resume_work.resume_hope_work_work1) >= 1:
                        answer_work += 1
                if answer_field >= 1 and answer_work >= 1:
                    answer_list.append(resume_title)

                    #################################################################################

                    school1 = Resume_ElementarySchool.objects.filter(resume_elementary=resume_title)
                    school2 = Resume_MiddleSchool.objects.filter(resume_middle=resume_title)
                    school3 = Resume_HighSchool.objects.filter(resume_high=resume_title)
                    school4 = Resume_UniversitySchool.objects.filter(resume_university=resume_title)

                    major = Resume_UniversitySchool_Major(resume_university_major=resume_title)





        context['answer_list'] = answer_list

    return render(request, 'search_resume.html', context)


