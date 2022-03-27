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
        print(request.POST, '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        field_list = request.POST.getlist('accordion2')
        work_list = request.POST.getlist('work2')
        study_list = request.POST.getlist('study1')
        return redirect('searchapp:search_resume2', field=field_list, work=work_list, study=study_list)
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
                    if temp.elementary_state:
                        answer.append(temp.elementary_state)
                    else:
                        answer.append("None")
                if school2.count() >= 1:
                    for temp in school2:
                        answer.append(temp.middle_school_name)
                    if temp.middle_state:
                        answer.append(temp.middle_state)
                    else:
                        answer.append("None")
                if school3.count() >= 1:
                    for temp in school3:
                        a = temp.high_school_name
                        b = temp.high_major
                    c = a + '(' + b + ')'
                    answer.append(c)
                    if temp.high_state:
                        answer.append(temp.high_state)
                    else:
                        answer.append("None")
                if school4.count() >= 1:
                    for temp in school4:
                        a = temp.university_school_name
                    if major.count() >= 1:
                        for temp in major:
                            b = temp.resume_university_major_detail
                            break
                    c = a + '(' + b + ')'
                    answer.append(c)
                    for temp in school4:
                        if temp.university_state:
                            answer.append(temp.university_state)
                        else:
                            answer.append("None")

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

def search_resume2(request, field, work, study):
    context = {}
    # print(field, '원래field?')
    # field = field.strip("[""]")
    # field = field.replace("'", "")
    # print(field)
    # work = work.strip("[""]")
    # work = work.replace("'", "")
    # list_field = field.split(',')
    # list_work = work.split(',')

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
                # print(field_list, 'field_list')
                # print(work_list, 'work_list')
                field_list.append(request.GET.get('field'))
                work_list.append(request.GET.get('work'))
                # print(field_list, 'field_list2')
                # print(work_list, 'work_list2')
                answer_field = 0
                answer_work = 0
                for resume_field in temp_field:
                    # print(resume_field.resume_hope_work_field1, '22222222222')
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
    study_list = []
    print(field, 'field')
    print(work, 'work')
    print(study, 'study')
    temp_study = '없음'
    for resume_title in temp_resume:
        if resume_title.resume_open == 1:
            temp_field = Resume_Hope_Work_Field.objects.filter(resume_hope_work_field=resume_title)
            temp_work = Resume_Hope_Work_Work.objects.filter(resume_hope_work_work=resume_title)

            school11 = Resume_ElementarySchool.objects.filter(resume_elementary=resume_title)
            school22 = Resume_MiddleSchool.objects.filter(resume_middle=resume_title)
            school33 = Resume_HighSchool.objects.filter(resume_high=resume_title)
            school44 = Resume_UniversitySchool.objects.filter(resume_university=resume_title)

            if school11.count() >= 1:
                for school111 in school11:
                    if school111.elementary_state == '중퇴':
                        temp_study = '고교졸업이하'
                    else:
                        temp_study = '고교졸업이하'
            if school22.count() >= 1:
                for school222 in school22:
                    if school222.middle_state == '중퇴':
                        temp_study = '고교졸업이하'
                    else:
                        temp_study = '고교졸업이하'
            if school33.count() >= 1:
                for school333 in school33:
                    if school333.high_state == '졸업':
                        temp_study = '고등학교졸업'
                    else:
                        temp_study = '고교졸업이하'
            if school44.count() >= 1:
                for school444 in school44:
                    if school444.university_state == '졸업' and school44.university_study_year == '대학(2,3년)':
                        temp_study = '대학 졸업(2,3년제)'
                    elif school444.university_state == '졸업' and school44.university_study_year == '대학교(4년)':
                        temp_study = '대학교 졸업(4년제)'
                    elif school444.university_state == '졸업' and school44.university_study_year == '대학원(석사)':
                        temp_study = '대학원 석사 졸업'
                    elif school444.university_state == '졸업' and school44.university_study_year == '대학원(박사)':
                        temp_study = '대학원 박사 졸업'
                    else:
                        temp_study = '고등학교졸업'

            answer_field = 0
            answer_work = 0
            answer_study = 0
            for resume_field in temp_field:
                # print(list_field, '11111111111111111111111111')
                # print(resume_field.resume_hope_work_field1, '22222222222')
                # print(resume_field.resume_hope_work_field1, resume_field.resume_hope_work_field)
                # print(list_field, 'list_field')
                print(field, 'field')
                if resume_field.resume_hope_work_field1 == '서울전체 서울':
                    if '서울' in field:
                        answer_field += 1
                if '서울전체 서울' in field:
                    if '서울' in resume_field.resume_hope_work_field1:
                        answer_field += 1
                if resume_field.resume_hope_work_field1 == '경기전체 경기':
                    if '경기' in field:
                        answer_field += 1
                if '경기전체 경기' in field:
                    if '경기' in resume_field.resume_hope_work_field1:
                        answer_field += 1
                if resume_field.resume_hope_work_field1 == '광주전체 광주':
                    if '광주' in field:
                        answer_field += 1
                if '광주전체 광주' in field:
                    if '광주' in resume_field.resume_hope_work_field1:
                        answer_field += 1
                if resume_field.resume_hope_work_field1 == '대구전체 대구':
                    if '대구' in field:
                        answer_field += 1
                if '대구전체 대구' in field:
                    if '대구' in resume_field.resume_hope_work_field1:
                        answer_field += 1
                if resume_field.resume_hope_work_field1 == '대전전체 대전':
                    if '대전' in field:
                        answer_field += 1
                if '대전전체 대전' in field:
                    if '대전' in resume_field.resume_hope_work_field1:
                        answer_field += 1
                if resume_field.resume_hope_work_field1 == '울산전체 울산':
                    if '울산' in field:
                        answer_field += 1
                if '울산전체 울산' in field:
                    if '울산' in resume_field.resume_hope_work_field1:
                        answer_field += 1
                if resume_field.resume_hope_work_field1 == '인천전체 인천':
                    if '인천' in field:
                        answer_field += 1
                if '인천전체 인천' in field:
                    if '인천' in resume_field.resume_hope_work_field1:
                        answer_field += 1
                if resume_field.resume_hope_work_field1 == '강원전체 강원':
                    if '강원' in field:
                        answer_field += 1
                if '강원전체 강원' in field:
                    if '강원' in resume_field.resume_hope_work_field1:
                        answer_field += 1
                if resume_field.resume_hope_work_field1 == '경남전체 경남':
                    if '경남' in field:
                        answer_field += 1
                if '경남전체 경남' in field:
                    if '경남' in resume_field.resume_hope_work_field1:
                        answer_field += 1
                if resume_field.resume_hope_work_field1 == '경북전체 경북':
                    if '경북' in field:
                        answer_field += 1
                if '경북전체 경북' in field:
                    if '경북' in resume_field.resume_hope_work_field1:
                        answer_field += 1
                if resume_field.resume_hope_work_field1 == '전남전체 전남':
                    if '전남' in field:
                        answer_field += 1
                if '전남전체 전남' in field:
                    if '전남' in resume_field.resume_hope_work_field1:
                        answer_field += 1
                if resume_field.resume_hope_work_field1 == '전북전체 전북':
                    if '전북' in field:
                        answer_field += 1
                if '전북전체 전북' in field:
                    if '전북' in resume_field.resume_hope_work_field1:
                        answer_field += 1
                if resume_field.resume_hope_work_field1 == '충북전체 충북':
                    if '충북' in field:
                        answer_field += 1
                if '충북전체 충북' in field:
                    if '충북' in resume_field.resume_hope_work_field1:
                        answer_field += 1
                if resume_field.resume_hope_work_field1 == '충남전체 충남':
                    if '충남' in field:
                        answer_field += 1
                if '충남전체 충남' in field:
                    if '충남' in resume_field.resume_hope_work_field1:
                        answer_field += 1
                if resume_field.resume_hope_work_field1 == '제주전체 제주':
                    if '제주' in field:
                        answer_field += 1
                if '제주전체 제주' in field:
                    if '제주' in resume_field.resume_hope_work_field1:
                        answer_field += 1
                if field.count(resume_field.resume_hope_work_field1) >= 1:
                    # print('실행중?')
                    answer_field += 1
            for resume_work in temp_work:
                if work.count(resume_work.resume_hope_work_work1) >= 1:
                    answer_work += 1
            print(temp_study, 'temp_study')
            for resume_study in temp_study:
                if study.count('학력무관') >= 1:
                    answer_study += 1
                if study.count(resume_study) >= 1:
                    print('이거 실행중>>>>>')
                    answer_study += 1
            if len(field) == 2:
                print('이거 실행안됌????')
                answer_field += 1
            if len(work) == 2:
                print('이거 실행안됌????')
                answer_work += 1
            if len(study) == 2:
                print('이거 실행안됌????')
                answer_study += 1
            if answer_field >= 1 and answer_work >= 1 and answer_study >= 1:
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
                    if temp.elementary_state:
                        answer.append(temp.elementary_state)
                    else:
                        answer.append("None")
                if school2.count() >= 1:
                    for temp in school2:
                        answer.append(temp.middle_school_name)
                    if temp.middle_state:
                        answer.append(temp.middle_state)
                    else:
                        answer.append("None")
                if school3.count() >= 1:
                    for temp in school3:
                        a = temp.high_school_name
                        b = temp.high_major
                    c = a + '(' + b + ')'
                    answer.append(c)
                    if temp.high_state:
                        answer.append(temp.high_state)
                    else:
                        answer.append("None")
                if school4.count() >= 1:
                    for temp in school4:
                        a = temp.university_school_name
                    if major.count() >= 1:
                        for temp in major:
                            b = temp.resume_university_major_detail
                            break
                    c = a + '(' + b + ')'
                    answer.append(c)
                    for temp in school4:
                        if temp.university_state:
                            answer.append(temp.university_state)
                        else:
                            answer.append("None")

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
    # print(answer_list)
    context['school_list'] = school_list

    page = request.GET.get('page_search', '1')

    count = len(answer_list)

    paginator = Paginator(answer_list, 8)

    page_obj = paginator.get_page(page)

    context['resume_search'] = page_obj
    context['count'] = count

    return render(request, 'search_resume2.html', context)


