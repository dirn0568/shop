
from django.http import request

# Create your views here.
from django.shortcuts import render

from accountapp.models import MyUser
from resumeapp.models import Resume_Title, Resume_Hope_Work_Field, Resume_Hope_Work_Work, Resume_ElementarySchool, \
    Resume_MiddleSchool, Resume_HighSchool, Resume_UniversitySchool, Resume_UniversitySchool_Major, Resume_Hope_Work


def search_resume(request):
    context = {}

    if request.method == 'POST' and request.POST.get('resume_submit1'):
        print(request.POST)
        temp_resume = Resume_Title.objects.all()
        answer_list = []
        school_list = []
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
                    # answer_list.append(resume_title)
                    #
                    # print(resume_title)
                    # print(resume_title.resume_elementary)
                    #################################################################################
                    answer = []
                    answer.append(resume_title)
                    answer.append(resume_title.resume_title_detail)
                    answer.append(resume_title.resume_date)

                    school1 = Resume_ElementarySchool.objects.filter(resume_elementary=resume_title)
                    school2 = Resume_MiddleSchool.objects.filter(resume_middle=resume_title)
                    school3 = Resume_HighSchool.objects.filter(resume_high=resume_title)
                    school4 = Resume_UniversitySchool.objects.filter(resume_university=resume_title)

                    major = Resume_UniversitySchool_Major.objects.filter(resume_university_major=resume_title)

                    if school1.count() >= 1:
                        for temp in school1:
                            answer.append(temp.elementary_school_name)
                    if school2.count() >= 1:
                        for temp in school2:
                            answer.append(temp_resume.middle_school_name)
                    if school3.count() >= 1:
                        for temp in school3:
                            a = temp.high_school_name
                            b = temp.high_major
                        c = a + '(' + b + ')'
                        answer.append(c)
                    if school4.count() >= 1:
                        for temp in school4:
                            a = temp.university_school_name
                        print(school1, '5555555555555555555555555555555555')
                        print(school2, '5555555555555555555555555555555555')
                        print(school3, '5555555555555555555555555555555555')
                        print(school4, '5555555555555555555555555555555555')
                        print(major,'5555555555555555555555555555555555')
                        if major.count() >= 1:
                            for temp in major:
                                b = temp.resume_university_major_detail
                                break
                        print('이거샐행중국??????')
                        c = a + '(' + b + ')'
                        answer.append(c)

                    hope_money = Resume_Hope_Work.objects.filter(resume_hope_work=resume_title)
                    for hope in hope_money:
                        answer.append(hope.resume_hope_work_money)

                    hope_field = Resume_Hope_Work_Field.objects.filter(resume_hope_work_field=resume_title)
                    for hope in hope_field:
                        answer.append(hope.resume_hope_work_field1)
                    hope_work = Resume_Hope_Work_Work.objects.filter(resume_hope_work_work=resume_title)
                    for hope in hope_work:
                        answer.append(hope.resume_hope_work_work1)

                    answer_list.append(answer)


        context['answer_list'] = answer_list
        context['school_list'] = school_list

    return render(request, 'search_resume.html', context)


