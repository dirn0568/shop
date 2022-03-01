from django.core.paginator import Paginator
from django.http import request

# Create your views here.
from django.shortcuts import render, redirect

from datetime import datetime

from accountapp.models import MyUser
from messageapp.models import Message_Send_Model
from profileapp.models import User_Profile
from resumeapp.models import Resume_Title, Resume_Hope_Work_Field, Resume_Hope_Work_Work, Resume_ElementarySchool, \
    Resume_MiddleSchool, Resume_HighSchool, Resume_UniversitySchool, Resume_UniversitySchool_Major, Resume_Hope_Work


def search_resume(request):
    context = {}

    title = request.GET.get('title', None)

    if title != None:
        resume = Resume_Title.objects.filter(pk=title)
        for temp_resume in resume:
            model = Message_Send_Model(message_send_receive=temp_resume.resume_title, message_send_send=request.user, message_send_detail="{0}회원님이 {1}이력서를 보고 회원님께 면접을 제의했습니다.".format(request.user, temp_resume.resume_title_detail))
            model.save()


    if request.method == 'POST' and request.POST.get('resume_submit1'):
        field_list = request.POST.getlist('accordion2')
        work_list = request.POST.getlist('work2')
        return redirect('searchapp:search_resume2', field=field_list, work=work_list)
        # return render(request, 'search_resume2.html', context)

    else:
        temp_resume = Resume_Title.objects.all()
        answer_list = []
        school_list = []
        for resume_title in temp_resume:
            if resume_title.resume_open == 1:
                answer = []
                answer.append(resume_title)

                ###############################################################

                # print(resume_title.resume_title.profile)
                temp_profile = User_Profile.objects.filter(profile=resume_title.resume_title)
                if temp_profile:
                    for profile in temp_profile:
                        if profile.user_name:
                            answer.append(profile.user_name)
                        else:
                            answer.append("None")

                        if profile.user_gender:
                            answer.append(profile.user_gender)
                        else:
                            answer.append("None")

                        if profile.user_birthday:
                            now = datetime.now()
                            date = now.strftime("%Y")
                            date2 = profile.user_birthday[:4]
                            date3 = int(date) - int(date2)

                            date4 = now.strftime("%m")
                            date5 = now.strftime("%d")
                            date6 = profile.user_birthday[4:6]
                            date7 = profile.user_birthday[6:9]
                            date4 = int(date4)
                            date5 = int(date5)
                            date6 = int(date6)
                            date7 = int(date7)
                            if date4 > date6:
                                pass
                            elif date4 == date6 and date5 >= date7:
                                pass
                            else:
                                date3 = date3 - 1
                            answer.append(date3)
                            answer.append(profile.user_birthday[:4])
                        else:
                            answer.append("None")
                            answer.append("None")
                else:
                    answer.append("None")
                    answer.append("None")
                    answer.append("None")
                    answer.append("None")

                #################################################################################

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
                        answer.append(temp.middle_school_name)
                if school3.count() >= 1:
                    for temp in school3:
                        a = temp.high_school_name
                        b = temp.high_major
                    c = a + '(' + b + ')'
                    answer.append(c)
                if school4.count() >= 1:
                    for temp in school4:
                        a = temp.university_school_name
                    if major.count() >= 1:
                        for temp in major:
                            b = temp.resume_university_major_detail
                            break
                    c = a + '(' + b + ')'
                    answer.append(c)

                hope_money = Resume_Hope_Work.objects.filter(resume_hope_work=resume_title)
                for hope in hope_money:
                    answer.append(hope.resume_hope_work_money)

                hope_field = Resume_Hope_Work_Field.objects.filter(resume_hope_work_field=resume_title)
                hope_list = []
                for hope in hope_field:
                    hope_list.append(hope.resume_hope_work_field1)
                answer.append(hope_list)

                hope_work = Resume_Hope_Work_Work.objects.filter(resume_hope_work_work=resume_title)
                hope_list2 = []
                for hope in hope_work:
                    hope_list2.append(hope.resume_hope_work_work1)
                answer.append(hope_list2)

                answer_list.append(answer)

        page = request.GET.get('page', '1')

        count = len(answer_list)

        paginator = Paginator(answer_list, 8)

        page_obj = paginator.get_page(page)

        context['resume'] = page_obj
        context['count'] = count

        context['answer'] = "None"
    return render(request, 'search_resume.html', context)

def search_resume2(request, field, work):
    context = {}
    field = field.strip("[""]")
    field = field.replace("'", "")
    work = work.strip("[""]")
    work = work.replace("'", "")
    list_field = field.split(',')
    list_work = work.split(',')

    title = request.GET.get('title', None)

    if title != None:
        resume = Resume_Title.objects.filter(pk=title)
        for temp_resume in resume:
            model = Message_Send_Model(message_send_receive=temp_resume.resume_title, message_send_send=request.user, message_send_detail="{0}회원님이 {1}이력서를 보고 회원님께 면접을 제의했습니다.".format(request.user, temp_resume.resume_title_detail))
            model.save()


    if request.method == 'POST' and request.POST.get('resume_submit1'):
        temp_resume = Resume_Title.objects.all()
        answer_list = []
        school_list = []
        for resume_title in temp_resume:
            if resume_title.resume_open == 1:
                temp_field = Resume_Hope_Work_Field.objects.filter(resume_hope_work_field=resume_title)
                temp_work = Resume_Hope_Work_Work.objects.filter(resume_hope_work_work=resume_title)
                field_list = request.POST.getlist('accordion2')
                work_list = request.POST.getlist('work2')
                field_list.append(request.GET.get('field'))
                work_list.append(request.GET.get('work'))
                answer_field = 0
                answer_work = 0
                for resume_field in temp_field:
                    print(resume_field.resume_hope_work_field1, '22222222222')
                    if field_list.count(resume_field.resume_hope_work_field1) >= 1:
                        answer_field += 1
                for resume_work in temp_work:
                    if work_list.count(resume_work.resume_hope_work_work1) >= 1:
                        answer_work += 1
                if answer_field >= 1 and answer_work >= 1:
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
                            answer.append(temp.middle_school_name)
                    if school3.count() >= 1:
                        for temp in school3:
                            a = temp.high_school_name
                            b = temp.high_major
                        c = a + '(' + b + ')'
                        answer.append(c)
                    if school4.count() >= 1:
                        for temp in school4:
                            a = temp.university_school_name
                        if major.count() >= 1:
                            for temp in major:
                                b = temp.resume_university_major_detail
                                break
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

        context['field'] = request.POST.getlist('accordion2')
        context['work'] = request.POST.getlist('work2')

        context['answer_list'] = answer_list
        context['school_list'] = school_list
        return redirect('searchapp:search_resume2', field=field_list, work=work_list)

    ###########################################################################################################################

    temp_resume = Resume_Title.objects.all()
    answer_list = []
    school_list = []
    for resume_title in temp_resume:
        if resume_title.resume_open == 1:
            temp_field = Resume_Hope_Work_Field.objects.filter(resume_hope_work_field=resume_title)
            temp_work = Resume_Hope_Work_Work.objects.filter(resume_hope_work_work=resume_title)
            answer_field = 0
            answer_work = 0
            for resume_field in temp_field:
                print(list_field, '11111111111111111111111111')
                print(resume_field.resume_hope_work_field1, '22222222222')
                if list_field.count(resume_field.resume_hope_work_field1) >= 1:
                    answer_field += 1
            for resume_work in temp_work:
                if list_work.count(resume_work.resume_hope_work_work1) >= 1:
                    answer_work += 1
            if answer_field >= 1 and answer_work >= 1:
                #################################################################################
                answer = []
                answer.append(resume_title)

                ###############################################################
                # print(resume_title.resume_title.profile)
                temp_profile = User_Profile.objects.filter(profile=resume_title.resume_title)
                if temp_profile:
                    for profile in temp_profile:
                        if profile.user_name:
                            answer.append(profile.user_name)
                        else:
                            answer.append("None")

                        if profile.user_gender:
                            answer.append(profile.user_gender)
                        else:
                            answer.append("None")

                        if profile.user_birthday:
                            now = datetime.now()
                            date = now.strftime("%Y")
                            date2 = profile.user_birthday[:4]
                            date3 = int(date) - int(date2)

                            date4 = now.strftime("%m")
                            date5 = now.strftime("%d")
                            date6 = profile.user_birthday[4:6]
                            date7 = profile.user_birthday[6:9]
                            date4 = int(date4)
                            date5 = int(date5)
                            date6 = int(date6)
                            date7 = int(date7)
                            if date4 > date6:
                                pass
                            elif date4 == date6 and date5 >= date7:
                                pass
                            else:
                                date3 = date3 - 1
                            answer.append(date3)
                            answer.append(profile.user_birthday[:4])
                        else:
                            answer.append("None")
                            answer.append("None")
                else:
                    answer.append("None")
                    answer.append("None")
                    answer.append("None")
                    answer.append("None")

                #################################################################################

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
                        answer.append(temp.middle_school_name)
                if school3.count() >= 1:
                    for temp in school3:
                        a = temp.high_school_name
                        b = temp.high_major
                    c = a + '(' + b + ')'
                    answer.append(c)
                if school4.count() >= 1:
                    for temp in school4:
                        a = temp.university_school_name
                    if major.count() >= 1:
                        for temp in major:
                            b = temp.resume_university_major_detail
                            break
                    c = a + '(' + b + ')'
                    answer.append(c)

                hope_money = Resume_Hope_Work.objects.filter(resume_hope_work=resume_title)
                for hope in hope_money:
                    answer.append(hope.resume_hope_work_money)

                hope_field = Resume_Hope_Work_Field.objects.filter(resume_hope_work_field=resume_title)
                hope_list = []
                for hope in hope_field:
                    hope_list.append(hope.resume_hope_work_field1)
                answer.append(hope_list)

                hope_work = Resume_Hope_Work_Work.objects.filter(resume_hope_work_work=resume_title)
                hope_list2 = []
                for hope in hope_work:
                    hope_list2.append(hope.resume_hope_work_work1)
                answer.append(hope_list2)

                answer_list.append(answer)

    context['answer_list'] = answer_list
    print(answer_list)
    context['school_list'] = school_list

    page = request.GET.get('page_search', '1')

    count = len(answer_list)

    paginator = Paginator(answer_list, 2)

    page_obj = paginator.get_page(page)

    context['resume_search'] = page_obj
    context['count'] = count

    return render(request, 'search_resume2.html', context)


