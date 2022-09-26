from django.http import Http404
from django.shortcuts import render, redirect

from datetime import datetime

# Create your views here.
from accountapp.models import MyUser
from messageapp.models import Message_Resume_Model, Message_Propose_Model
from profileapp.models import User_Profile
from resumeapp.forms import ResumeForm, Update_ResumeForm, ResumeElementaryForm, ResumeMiddleForm, ResumeHighForm, \
    ResumeUniversityForm, ResumeUniversitySchoolMajor_Form, ResumeTitleForm, ResumeCareerForm, ResumeCareerAbilityForm, \
    ResumeCareerProjectForm, ResumeOutPlay, ResumePrizePlay, ResumePortPolio, ResumeSelfIntroduce, ResumeHopeWorkForm, \
    ResumeHopeWorkFieldForm, ResumeHopeWorkWorkForm
from resumeapp.models import User_Resume, User_Resume_Certificate, Resume_Title, Resume_ElementarySchool, \
    Resume_MiddleSchool, Resume_HighSchool, Resume_UniversitySchool, Resume_UniversitySchool_Major, Resume_Out_Play, \
    Resume_Prize_Play, Resume_Port_Polio, Resume_Self_Introduce, Resume_Career, Resume_Career_Ability, \
    Resume_Career_Project, Resume_Hope_Work, Resume_Hope_Work_Field, Resume_Hope_Work_Work, Resume_Like


def create_resume(request, pk):
    temp_user = MyUser.objects.filter(pk=pk)
    for user_test in temp_user:
        if request.user == user_test:
            pass
        else:
            raise Http404("잘못된 접근입니다")
    if request.method == "POST":
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            temp_form = form.save(commit=False)
            for temp in temp_user:
                temp_form.resume = temp
            temp_form.save()
            return redirect('accountapp:detail_user', pk)
    context = {}
    context['resume_form'] = ResumeForm
    context['pk'] = pk
    return render(request, 'create_resume.html', context)

def update_resume(request, pk):
    temp_user = MyUser.objects.filter(pk=pk)
    for user_test in temp_user:
        if request.user == user_test:
            pass
        else:
            raise Http404("잘못된 접근입니다")
    if request.method == "POST":
        form = Update_ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            for temp in temp_user:
                temp_resume = User_Resume.objects.filter(resume=temp)
            for temp in temp_resume:
                if len(request.POST['resume_school']) != 0:
                    temp.resume_school = request.POST['resume_school']
                if len(request.POST['resume_career']) != 0:
                    temp.resume_career = request.POST['resume_career']
                if request.FILES:
                    temp.resume_certificate = request.FILES['resume_certificate']
                temp.save()
            return redirect('accountapp:detail_user', pk)
    context = {}
    context['resume_form'] = Update_ResumeForm
    context['pk'] = pk
    return render(request, 'update_resume.html', context)

def delete_resume(request, pk):
    temp_user = MyUser.objects.filter(pk=pk)
    for user_test in temp_user:
        if request.user == user_test:
            pass
        else:
            raise Http404("잘못된 접근입니다")
    if request.method == "POST":
        for temp in temp_user:
            temp_resume = User_Resume.objects.filter(resume=temp)
        for temp in temp_resume:
            temp.delete()
        return redirect('accountapp:detail_user', pk)
    context = {}
    context['pk'] = pk
    return render(request, 'delete_resume.html', context)

def list_resume(request, title, pk):
    temp_user = MyUser.objects.filter(pk=pk)
    if request.method == "POST" and request.POST.get('resume_submit1'):
        temp_resume = Resume_Title.objects.filter(pk=title)
        print('실행중??????????????????????????12414124124?')
        for resume in temp_resume:
            if resume.resume_open == 1:
                resume.resume_open = 2
            elif resume.resume_open == 2:
                resume.resume_open = 0
            else:
                resume.resume_open = 1
            resume.save()

    for user_test in temp_user:
        for temp in temp_user:
            temp_resume = Resume_Title.objects.filter(resume_title=temp)
        context = {}
        context['pk'] = pk
        context['resume'] = temp_resume
    return render(request, 'list_resume.html', context)

def detail_resume(request, title):
    context = {}

    resume = Resume_Title.objects.filter(pk=title)
    ##########################################################################################################
    # profile

    for temp_resume in resume:
        user = temp_resume.resume_title
        profile = User_Profile.objects.filter(profile=user)
    if profile:
        for temp_profile in profile:
            if temp_profile.user_open == 1:
                print(temp_profile.profile_img, '이미지 어떻게 나옴')
                if temp_profile.profile_img:
                    context['profile_img'] = temp_profile.profile_img
                else:
                    context['profile_img'] = "None"
                if temp_profile.user_name:
                    temp_name = temp_profile.user_name[0:1]
                    for i in range(len(temp_profile.user_name) - 1):
                        temp_name += 'O'
                    context['user_name'] = temp_name
                else:
                    context['user_name'] = "None"
                if temp_profile.user_birthday:
                    now = datetime.now()
                    date = now.strftime("%Y")
                    date2 = temp_profile.user_birthday[:4]
                    date3 = int(date) - int(date2)

                    date4 = now.strftime("%m")
                    date5 = now.strftime("%d")
                    date6 = temp_profile.user_birthday[4:6]
                    date7 = temp_profile.user_birthday[6:9]
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
                    context['user_birthday'] = date3
                else:
                    context['user_birthday'] = "None"
                if temp_profile.user_gender:
                    context['user_gender'] = temp_profile.user_gender
                else:
                    context['user_gender'] = "None"
                if temp_profile.phone_number:
                    context['phone_number'] = '010-****-****'
                else:
                    context['phone_number'] = "None"
                if temp_profile.user_email:
                    context['user_email'] = '***@************'
                else:
                    context['user_email'] = "None"
                if temp_profile.user_page:
                    context['user_page'] = 'http://****************************'
                else:
                    context['user_page'] = "None"
            else:
                context['profile_img'] = "None"
                context['user_name'] = "None"
                context['user_birthday'] = "None"
                context['user_gender'] = "None"
                context['phone_number'] = "None"
                context['user_email'] = "None"
                context['user_page'] = "None"
    else:
        context['profile_img'] = "None"
        context['user_name'] = "None"
        context['user_birthday'] = "None"
        context['user_gender'] = "None"
        context['phone_number'] = "None"
        context['user_email'] = "None"
        context['user_page'] = "None"


    ##########################################################################################################
    # resume_like
    page = request.GET.get('like_user', None)

    if page != None:
        user = MyUser.objects.filter(pk=page)
        for temp_user in user:
            for temp_resume in resume:
                like_filter = Resume_Like.objects.filter(resume_like_resume=temp_resume, resume_like_user=temp_user)
                if like_filter:
                    like_filter.delete()
                    temp_resume.like_vote -= 1
                    temp_resume.save()
                else:
                    like = Resume_Like(resume_like_resume=temp_resume, resume_like_user=temp_user)
                    like.save()
                    temp_resume.like_vote += 1
                    temp_resume.save()

    for temp_resume in resume:
        resume_like = Resume_Like.objects.filter(resume_like_resume=temp_resume)
        resume_like_list = []
        for temp_like in resume_like:
            resume_like_list.append(temp_like.resume_like_user.pk)
        if resume_like_list.count(request.user.pk) >= 1:
            context['like'] = 1
        else:
            context['like'] = 0
    for temp_resume in resume:
        context['like_count'] = temp_resume.like_vote
    ################################################################################################################################
    # resume_propose
    resume_propose = request.GET.get('resume_propose', None)

    if resume_propose != None:
        for temp_resume in resume:
            resume = Resume_Title.objects.filter(pk=title)
            model = Message_Propose_Model(message_propose_receive=temp_resume.resume_title, message_propose_send=request.user, message_propose_detail="{0}회원({1})님이 {2}이력서를 보고 회원님께 면접을 제의했습니다. 회사명 : {1} 채용담당자 : {0}".format(request.user, request.user.company_name ,temp_resume.resume_title_detail),
                                          message_propose_company_group=request.user.company_group, message_propose_company_name=request.user.company_name, message_propose_company_ceo=request.user.company_ceo, message_propose_company_logo=request.user.company_logo, message_propose_company_phone_number=request.user.company_phone_number, message_propose_resume_title=temp_resume.resume_title_detail)
            model.save()



    #############################################################################################################

    for temp_resume in resume:
        if request.user.pk == None or temp_resume.resume_title == request.user:
            pass
        else:
            user = MyUser.objects.filter(pk=temp_resume.resume_title.pk)
            for temp_user in user:
                print("01-28 실행중?????")
                Message_Resume_Model(message_resume_receive=temp_user, message_resume_send=request.user, message_detail='{0}님이 회원님의 이력서 {1}을 열람해보았습니다.'.format(request.user, temp_resume.resume_title_detail)).save()
                # print(request.POST.get('school1{0}'.format(i)))

    if request.method == 'POST' and request.POST.get('resume_school_del'):
        temp_resume = Resume_Title.objects.filter(pk=title)
        for user_resume in temp_resume:
            find_resume = Resume_ElementarySchool.objects.filter(resume_elementary=user_resume)
            find_resume.delete()
            find_resume = Resume_MiddleSchool.objects.filter(resume_middle=user_resume)
            find_resume.delete()
            find_resume = Resume_HighSchool.objects.filter(resume_high=user_resume)
            find_resume.delete()
            find_resume = Resume_UniversitySchool.objects.filter(resume_university=user_resume)
            find_resume.delete()
            find_resume = Resume_UniversitySchool_Major.objects.filter(resume_university_major=user_resume)
            find_resume.delete()
        return redirect('resumeapp:detail_resume', title=title)

    if request.method == 'POST' and request.POST.get('resume_career_del'):
        print('이거실행중????????????????????')
        temp_resume = Resume_Title.objects.filter(pk=title)
        for user_resume in temp_resume:
            find_resume = Resume_Career.objects.filter(resume_career=user_resume)
            find_resume.delete()
            find_resume = Resume_Career_Ability.objects.filter(resume_career_ability=user_resume)
            find_resume.delete()
            find_resume = Resume_Career_Project.objects.filter(resume_career_project=user_resume)
            find_resume.delete()
        return redirect('resumeapp:detail_resume', title=title)

    if request.method == 'POST' and request.POST.get('resume_hope_work_del'):
        temp_resume = Resume_Title.objects.filter(pk=title)
        for user_resume in temp_resume:
            find_resume = Resume_Hope_Work.objects.filter(resume_hope_work=user_resume)
            find_resume.delete()
            find_resume = Resume_Hope_Work_Field.objects.filter(resume_hope_work_field=user_resume)
            find_resume.delete()
            find_resume = Resume_Hope_Work_Work.objects.filter(resume_hope_work_work=user_resume)
            find_resume.delete()
        return redirect('resumeapp:detail_resume', title=title)

    if request.method == 'POST' and request.POST.get('resume_out_play_del'):
        temp_resume = Resume_Title.objects.filter(pk=title)
        for user_resume in temp_resume:
            find_resume = Resume_Out_Play.objects.filter(resume_out_play=user_resume)
            find_resume.delete()
        return redirect('resumeapp:detail_resume', title=title)

    if request.method == 'POST' and request.POST.get('resume_prize_play_del'):
        temp_resume = Resume_Title.objects.filter(pk=title)
        for user_resume in temp_resume:
            find_resume = Resume_Prize_Play.objects.filter(resume_prize_play=user_resume)
            find_resume.delete()
        return redirect('resumeapp:detail_resume', title=title)

    if request.method == 'POST' and request.POST.get('resume_port_polio_del'):
        temp_resume = Resume_Title.objects.filter(pk=title)
        for user_resume in temp_resume:
            find_resume = Resume_Port_Polio.objects.filter(resume_port_polio=user_resume)
            find_resume.delete()
        return redirect('resumeapp:detail_resume', title=title)

    if request.method == 'POST' and request.POST.get('resume_self_introduce_del'):
        temp_resume = Resume_Title.objects.filter(pk=title)
        for user_resume in temp_resume:
            find_resume = Resume_Self_Introduce.objects.filter(resume_self_introduce=user_resume)
            find_resume.delete()
        return redirect('resumeapp:detail_resume', title=title)


    temp_resume = Resume_Title.objects.filter(pk=title)
    for user_resume in temp_resume:
        school1 = Resume_ElementarySchool.objects.filter(resume_elementary=user_resume)
        school2 = Resume_MiddleSchool.objects.filter(resume_middle=user_resume)
        school3 = Resume_HighSchool.objects.filter(resume_high=user_resume)
        school4 = Resume_UniversitySchool.objects.filter(resume_university=user_resume)

        major = Resume_UniversitySchool_Major.objects.filter(resume_university_major=user_resume)

        out_play = Resume_Out_Play.objects.filter(resume_out_play=user_resume)
        prize_play = Resume_Prize_Play.objects.filter(resume_prize_play=user_resume)
        port_polio = Resume_Port_Polio.objects.filter(resume_port_polio=user_resume)
        self_introduce = Resume_Self_Introduce.objects.filter(resume_self_introduce=user_resume)

        resume_career = Resume_Career.objects.filter(resume_career=user_resume)
        resume_career_ability = Resume_Career_Ability.objects.filter(resume_career_ability=user_resume)
        resume_career_project = Resume_Career_Project.objects.filter(resume_career_project=user_resume)

        resume_hope_work = Resume_Hope_Work.objects.filter(resume_hope_work=user_resume)
        resume_hope_work_field = Resume_Hope_Work_Field.objects.filter(resume_hope_work_field=user_resume)
        resume_hope_work_work = Resume_Hope_Work_Work.objects.filter(resume_hope_work_work=user_resume)
        context['pk'] = user_resume.resume_title.pk
        context['title'] = title

        if len(school1) == 0 and len(school2) == 0 and len(school3) == 0 and len(school4) == 0:
            context['school'] = 1
        else:
            context['school1'] = school1
            context['school2'] = school2
            context['school3'] = school3
            context['school4'] = school4

        context['major'] = major

        if len(out_play) == 0:
            context['none_out_play'] = 1
        else:
            context['out_play'] = out_play
        if len(prize_play) == 0:
            context['none_prize_play'] = 1
        else:
            context['prize_play'] = prize_play
        if len(port_polio) == 0:
            context['none_port_polio'] = 1
        else:
            context['port_polio'] = port_polio
        if len(self_introduce) == 0:
            context['none_self_introduce'] = 1
        else:
            context['self_introduce'] = self_introduce

        if len(resume_career) == 0:
            context['none_resume_career'] = 1
        else:
            context['resume_career'] = resume_career
            context['resume_career_ability'] = resume_career_ability
            context['resume_career_project'] = resume_career_project

        if len(resume_hope_work) == 0:
            print("02-12 이거없냐?")
            context['none_resume_hope_work'] = 1
        else:
            for test in resume_hope_work:
                print(test.resume_hope_work_money, "02-12 이거있냐?")
            context['resume_hope_work'] = resume_hope_work
            context['resume_hope_work_field'] = resume_hope_work_field
            context['resume_hope_work_work'] = resume_hope_work_work
        context['resume'] = user_resume

    return render(request, 'detail_resume.html', context)

def test_resume(request, test1, test2, test3, pk):
    # 테스트 버전 1
    test_list1 = [[0]]
    test_list2 = [[0]]
    test_list3 = [[0]]
    temp_user = MyUser.objects.filter(pk=pk)
    resume_school_text = ''
    resume_career_text = ''
    if request.method == "GET":
        test1 = 1
        test2 = 1
        test3 = 1
    if request.method == "POST":
        if request.POST.get('button_test1'):
            test1 += 1
            for i in range(1, test1):
                test_list1.append([i])
            for i in range(1, test2):
                test_list2.append([i])
            for i in range(1, test3):
                test_list3.append([i])
            # for i in range(0, test1):
            #     a = 'school1' + str(i) # i의 번호가 틀려서 자꾸 오류뜸 11-12
            #     print(a, '##################################')
            #     # print(type(a))
            #     # print(request.POST)
            #     print(request.POST.get[a])
        if request.POST.get('button_test2'):
            test2 += 1
            for i in range(1, test1):
                test_list1.append([i])
            for i in range(1, test2):
                test_list2.append([i])
            for i in range(1, test3):
                test_list3.append([i])
        if request.POST.get('button_test3'):
            test3 += 1
            for i in range(1, test1):
                test_list1.append([i])
            for i in range(1, test2):
                test_list2.append([i])
            for i in range(1, test3):
                test_list3.append([i])
        if request.POST.get('button_test4'):
            temp_user = MyUser.objects.filter(pk=pk)
            print(request.POST)
            for i in range(0, test1):
                # print(request.POST.get('school1{0}'.format(i)))
                if request.POST.get('school1{0}'.format(i)) == None:
                    pass
                else:
                    resume_school_text += request.POST.get('school1{0}'.format(i))
            for i in range(0, test2):
                # print(request.POST.get('school2{0}'.format(i)))
                if request.POST.get('school2{0}'.format(i)) == None:
                    pass
                else:
                    resume_career_text += request.POST.get('school2{0}'.format(i))
            # for i in range(0, test3):
            #     # print(request.POST.get('school3{0}'.format(i)))
            #     if request.POST.get('school3{0}'.format(i)) == None:
            #         pass
            #     else:
            #         resume_certificate_test += request.POST.get('school3{0}'.format(i))
            # print(request.FILES)
            for temp in temp_user:
                User_Resume(resume=temp, resume_title=request.POST.get('school0'), resume_school=resume_school_text,
                            resume_career=resume_career_text, resume_text=request.POST.get('school4')).save()
            for i in range(0, test3):
                User_Resume_Certificate(certificate=User_Resume.objects.last(), resume_certificate=request.FILES.get('school3{0}'.format(i))).save()

    context={}
    context['pk'] = pk
    # print(test_list1)
    # print(test_list2)
    context['test_list1'] = test_list1
    context['test_list2'] = test_list2
    context['test_list3'] = test_list3
    context['test1'] = test1
    context['test2'] = test2
    context['test3'] = test3
    return render(request, 'test_resume.html', context)



#######################################################################################################


def resume_1(request, school, school_major4, career, pk):
    # 테스트 버전2
    temp_school_major4 = [[0]]
    context = {}
    context['school'] = school
    context['school_major4'] = school_major4
    context['career'] = career
    context['temp_school_major4'] = temp_school_major4
    context['pk'] = pk
    if request.method == 'POST' and request.POST.get('major_button_plus'):
        school_major4 += 1
        context['school_major4'] = school_major4
        for i in range(1, school_major4):
            temp_school_major4.append([i])
        context['temp_school_major4'] = temp_school_major4

    if request.method == 'POST' and request.POST.get('resume_submit1'):
        print('*******************************',request.POST,'&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
        print(request.POST['accordion1'], '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        temp_user = MyUser.objects.filter(pk=pk)
        form = ResumeTitleForm(request.POST, request.FILES)
        if form.is_valid():
            temp_form = form.save(commit=False)
            for temp in temp_user:
                temp_form.resume_title = temp
            temp_form.resume_title_detail = request.POST['resume_title']
            temp_form.save()
        if request.method == 'POST' and school == 1:
            form = ResumeElementaryForm(request.POST, request.FILES)
            if form.is_valid():
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    temp_form.resume_elementary = temp
                temp_form.elementary_school_name = request.POST['elementary_school_name']
                temp_form.elementary_field_name = request.POST['study_field1']
                temp_form.elementary_start_time = request.POST['study_start1']
                temp_form.elementary_end_time = request.POST['study_end1']
                temp_form.save()
        elif request.method == 'POST' and school == 2:
            form = ResumeMiddleForm(request.POST, request.FILES)
            if form.is_valid():
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    temp_form.resume_middle = temp
                temp_form.middle_school_name = request.POST['middle_school_name']
                temp_form.middle_field_name = request.POST['study_field2']
                temp_form.middle_start_time = request.POST['study_start2']
                temp_form.middle_end_time = request.POST['study_end2']
                temp_form.save()
        elif request.method == 'POST' and school == 3:
            form = ResumeHighForm(request.POST, request.FILES)
            if form.is_valid():
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    temp_form.resume_high = temp
                temp_form.high_school_name = request.POST['high_school_name']
                temp_form.high_field_name = request.POST['study_field3']
                temp_form.high_start_time = request.POST['study_start3']
                temp_form.high_end_time = request.POST['study_end3']
                temp_form.high_major = request.POST['study_major3']
                temp_form.save()
        elif request.method == 'POST' and school == 4:
            form = ResumeUniversityForm(request.POST, request.FILES)
            if form.is_valid():
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    temp_form.resume_university = temp
                temp_form.university_study_year = request.POST['study_year4']
                temp_form.university_school_name = request.POST['university_school_name']
                temp_form.university_field_name = request.POST['study_field4']
                temp_form.university_start_time = request.POST['study_start4']
                temp_form.university_end_time = request.POST['study_end4']
                temp_form.university_study_time = request.POST['study_time4']
                temp_form.university_study_level = request.POST['study_level4']
                temp_form.university_finaltest = request.POST['study_finaltest4']
                temp_form.save()
            if form.is_valid():
                for i in range(0, school_major4):
                    form = ResumeUniversitySchoolMajor_Form(request.POST, request.FILES)
                    temp_form = form.save(commit=False)
                    temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                    for temp in temp_title:
                        temp_form.resume_university_major = temp
                    # temp_form.resume_university_major = Resume_Title.objects.last()
                    temp_form.resume_university_major_list = request.POST.get('study_major_list4{0}'.format(i))
                    temp_form.resume_university_major_detail = request.POST.get('study_major_detail4{0}'.format(i))
                    temp_form.save() # 11-22 학과가 제대로 저장안됨 이력서 제목이 여러개 저장되는건지 확인해야함
            # study_major_list4
            # study_major_detail4
    return render(request, 'resume_1.html', context)

def test_test(request):
    if request.method == "POST":
        print(request.POST)
    context={}
    return render(request, 'test_test.html', context)

def test_test2(request):
    if request.method == 'POST':
        print('############test_test2##########', request.POST)
    context={}
    return render(request, 'test_test2.html', context)

def test_test3(request):
    context = {}
    # if test == 3:
    #     test3=[]
    #     test3.append(['광주전체'])
    #     test3.append(['광산구'])
    #     test3.append(['남구'])
    #     test3.append(['동구'])
    #     test3.append(['북구'])
    #     test3.append(['서구'])
    #     context['test3'] = test3

    return render(request, 'test_test3.html', context)





##########################################################################################################




def resume_resume1(request, pk):
    if request.method == 'POST':
        print(request.POST)
    context={}
    context['pk'] = pk
    return render(request, 'resume_resume1.html', context)

def resume_resume2(request, school, school_major4, career, out_play, prize_play, port_polio, self_introduce, pk):
    temp_school_major4 = [[0]]
    temp_out_play = []
    temp_prize_play = []
    temp_port_polio = []
    temp_self_introduce = []

    context = {}
    context['school'] = school
    context['school_major4'] = school_major4
    context['career'] = career
    context['out_play'] = out_play
    context['prize_play'] = prize_play
    context['port_polio'] = port_polio
    context['self_introduce'] = self_introduce

    context['temp_school_major4'] = temp_school_major4
    context['temp_out_play'] = temp_out_play
    context['temp_prize_play'] = temp_prize_play
    context['temp_port_polio'] = temp_port_polio
    context['temp_self_introduce'] = temp_self_introduce

    context['pk'] = pk
    if request.method == 'POST' and request.POST.get('major_button_plus'):
        school_major4 += 1
        context['school_major4'] = school_major4

    if request.method == 'POST' and request.POST.get('out_play_button'):
        out_play += 1
        context['out_play'] = out_play

    if request.method == 'POST' and request.POST.get('prize_play_button'):
        prize_play += 1
        context['prize_play'] = prize_play

    if request.method == 'POST' and request.POST.get('port_polio_button'):
        port_polio += 1
        context['port_polio'] = port_polio

    if request.method == 'POST' and request.POST.get('self_introduce_button'):
        self_introduce += 1
        context['self_introduce'] = self_introduce

    for i in range(1, school_major4):
        temp_school_major4.append([i])
    for i in range(0, out_play):
        temp_out_play.append([i])
    for i in range(0, prize_play):
        temp_prize_play.append([i])
    for i in range(0, port_polio):
        temp_port_polio.append([i])
    for i in range(0, self_introduce):
        temp_self_introduce.append([i])
    context['temp_school_major4'] = temp_school_major4
    context['temp_out_play'] = temp_out_play
    context['temp_prize_play'] = temp_prize_play
    context['temp_port_polio'] = temp_port_polio
    context['temp_self_introduce'] = temp_self_introduce

    if request.method == 'POST' and (request.POST.get('resume_submit1') or request.POST.get('resume_submit2')):
        print('*******************************', request.POST, '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
        temp_user = MyUser.objects.filter(pk=pk)
        form = ResumeTitleForm(request.POST, request.FILES)
        if form.is_valid():
            temp_form = form.save(commit=False)
            for temp in temp_user:
                temp_form.resume_title = temp
            temp_form.resume_title_detail = request.POST['resume_title']
            temp_form.save()
        if request.method == 'POST' and school == 1:
            form = ResumeElementaryForm(request.POST, request.FILES)
            if form.is_valid():
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    title = temp.pk
                    temp_form.resume_elementary = temp
                if request.POST.get('초졸검정고시') == 'on':
                    temp_form.elementary_school_name = '초졸검정고시'
                    temp_form.elementary_gamjang_time = request.POST['elementary_gamjang_day']
                    temp_form.elementary_state = '졸업'
                    temp_form.elementary_school_file = request.FILES.get('school_file1')
                    temp_form.save()
                else:
                    temp_form.elementary_school_name = request.POST['elementary_school_name']
                    temp_form.elementary_field_name = request.POST['study_field1']
                    temp_form.elementary_start_time = request.POST['study_start1']
                    temp_form.elementary_end_time = request.POST['study_end1']
                    temp_form.elementary_state = request.POST['elementary_state']
                    temp_form.elementary_school_file = request.FILES.get('school_file1')
                    temp_form.save()

            for i in range(0, out_play):
                form = ResumeOutPlay(request.POST, request.FILES)
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    temp_form.resume_out_play = temp
                temp_form.resume_out_activity = request.POST.get('out_play1{0}'.format(i))
                temp_form.resume_out_place = request.POST.get('out_play2{0}'.format(i))
                temp_form.resume_out_start_play = request.POST.get('out_play3{0}'.format(i))
                temp_form.resume_out_end_play = request.POST.get('out_play4{0}'.format(i))
                temp_form.resume_out_play_text = request.POST.get('out_play5{0}'.format(i))
                temp_form.save()

            for i in range(0, prize_play):
                form = ResumePrizePlay(request.POST, request.FILES)
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    temp_form.resume_prize_play = temp
                temp_form.resume_prize_certificate = request.POST.get('prize_play1{0}'.format(i))
                temp_form.resume_prize_place = request.POST.get('prize_play2{0}'.format(i))
                temp_form.resume_prize_title = request.POST.get('prize_play3{0}'.format(i))
                temp_form.resume_prize_date = request.POST.get('prize_play4{0}'.format(i))
                temp_form.save()

            for i in range(0, port_polio):
                form = ResumePortPolio(request.POST, request.FILES)
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    temp_form.resume_port_polio = temp
                temp_form.resume_port_polio_detail = request.FILES.get('port_polio1{0}'.format(i))
                temp_form.save()

            for i in range(0, self_introduce):
                form = ResumeSelfIntroduce(request.POST, request.FILES)
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    temp_form.resume_self_introduce = temp
                temp_form.resume_self_introduce_title = request.POST.get('self_introduce1{0}'.format(i))
                temp_introduce_text = request.POST.get('self_introduce2{0}'.format(i))
                data=''
                for temp_data in temp_introduce_text:
                    if temp_data == ' ':
                        data += '∠'
                    elif temp_data == '\r':
                        data += '∏'
                    else:
                        data += temp_data
                temp_form.resume_self_introduce_text = data
                temp_form.save()
        elif request.method == 'POST' and school == 2:
            form = ResumeMiddleForm(request.POST, request.FILES)
            if form.is_valid():
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    title = temp.pk
                    temp_form.resume_middle = temp
                if request.POST.get('중졸검정고시') == 'on':
                    temp_form.middle_school_name = '중졸검정고시'
                    temp_form.middle_gamjang_time = request.POST['middle_gamjang_day']
                    temp_form.middle_state = '졸업'
                    temp_form.middle_school_file = request.FILES.get('school_file2')
                    temp_form.save()
                else:
                    temp_form.middle_school_name = request.POST['middle_school_name']
                    temp_form.middle_field_name = request.POST['study_field2']
                    temp_form.middle_start_time = request.POST['study_start2']
                    temp_form.middle_end_time = request.POST['study_end2']
                    temp_form.middle_state = request.POST['middle_state']
                    temp_form.middle_school_file = request.FILES.get('school_file2')
                    temp_form.save()

            for i in range(0, out_play):
                form = ResumeOutPlay(request.POST, request.FILES)
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    temp_form.resume_out_play = temp
                temp_form.resume_out_activity = request.POST.get('out_play1{0}'.format(i))
                temp_form.resume_out_place = request.POST.get('out_play2{0}'.format(i))
                temp_form.resume_out_start_play = request.POST.get('out_play3{0}'.format(i))
                temp_form.resume_out_end_play = request.POST.get('out_play4{0}'.format(i))
                temp_form.resume_out_play_text = request.POST.get('out_play5{0}'.format(i))
                temp_form.save()

            for i in range(0, prize_play):
                form = ResumePrizePlay(request.POST, request.FILES)
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    temp_form.resume_prize_play = temp
                temp_form.resume_prize_certificate = request.POST.get('prize_play1{0}'.format(i))
                temp_form.resume_prize_place = request.POST.get('prize_play2{0}'.format(i))
                temp_form.resume_prize_title = request.POST.get('prize_play3{0}'.format(i))
                temp_form.resume_prize_date = request.POST.get('prize_play4{0}'.format(i))
                temp_form.save()

            for i in range(0, port_polio):
                form = ResumePortPolio(request.POST, request.FILES)
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    temp_form.resume_port_polio = temp
                temp_form.resume_port_polio_detail = request.FILES.get('port_polio1{0}'.format(i))
                temp_form.save()

            for i in range(0, self_introduce):
                form = ResumeSelfIntroduce(request.POST, request.FILES)
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    temp_form.resume_self_introduce = temp
                temp_form.resume_self_introduce_title = request.POST.get('self_introduce1{0}'.format(i))
                temp_form.resume_self_introduce_text = request.POST.get('self_introduce2{0}'.format(i))
                temp_form.save()
        elif request.method == 'POST' and school == 3:
            form = ResumeHighForm(request.POST, request.FILES)
            if form.is_valid():
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    title = temp.pk
                    temp_form.resume_high = temp
                if request.POST.get('고졸검정고시') == 'on':
                    temp_form.high_school_name = '고졸검정고시'
                    temp_form.high_gamjang_time = request.POST['high_gamjang_day']
                    temp_form.high_state = '졸업'
                    temp_form.high_school_file = request.FILES.get('school_file3')
                    temp_form.save()
                else:
                    temp_form.high_school_name = request.POST['high_school_name']
                    temp_form.high_field_name = request.POST['study_field3']
                    temp_form.high_start_time = request.POST['study_start3']
                    temp_form.high_end_time = request.POST['study_end3']
                    temp_form.high_major = request.POST['study_major3']
                    temp_form.high_state = request.POST['high_state']
                    temp_form.high_school_file = request.FILES.get('school_file3')
                    temp_form.save()

            for i in range(0, out_play):
                form = ResumeOutPlay(request.POST, request.FILES)
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    temp_form.resume_out_play = temp
                temp_form.resume_out_activity = request.POST.get('out_play1{0}'.format(i))
                temp_form.resume_out_place = request.POST.get('out_play2{0}'.format(i))
                temp_form.resume_out_start_play = request.POST.get('out_play3{0}'.format(i))
                temp_form.resume_out_end_play = request.POST.get('out_play4{0}'.format(i))
                temp_form.resume_out_play_text = request.POST.get('out_play5{0}'.format(i))
                temp_form.save()

            for i in range(0, prize_play):
                form = ResumePrizePlay(request.POST, request.FILES)
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    temp_form.resume_prize_play = temp
                temp_form.resume_prize_certificate = request.POST.get('prize_play1{0}'.format(i))
                temp_form.resume_prize_place = request.POST.get('prize_play2{0}'.format(i))
                temp_form.resume_prize_title = request.POST.get('prize_play3{0}'.format(i))
                temp_form.resume_prize_date = request.POST.get('prize_play4{0}'.format(i))
                temp_form.save()

            for i in range(0, port_polio):
                form = ResumePortPolio(request.POST, request.FILES)
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    temp_form.resume_port_polio = temp
                temp_form.resume_port_polio_detail = request.FILES.get('port_polio1{0}'.format(i))
                temp_form.save()

            for i in range(0, self_introduce):
                form = ResumeSelfIntroduce(request.POST, request.FILES)
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    temp_form.resume_self_introduce = temp
                temp_form.resume_self_introduce_title = request.POST.get('self_introduce1{0}'.format(i))
                temp_form.resume_self_introduce_text = request.POST.get('self_introduce2{0}'.format(i))
                temp_form.save()
        elif request.method == 'POST' and school == 4:
            form = ResumeUniversityForm(request.POST, request.FILES)
            if form.is_valid():
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    title = temp.pk
                    temp_form.resume_university = temp
                temp_form.university_study_year = request.POST['study_year4']
                temp_form.university_school_name = request.POST['university_school_name']
                temp_form.university_field_name = request.POST['study_field4']
                temp_form.university_start_time = request.POST['study_start4']
                temp_form.university_end_time = request.POST['study_end4']
                temp_form.university_study_time = request.POST['study_time4']
                temp_form.university_study_level = request.POST['study_level4']
                temp_form.university_finaltest = request.POST['study_finaltest4']
                temp_form.university_state = request.POST['university_state']
                temp_form.university_school_file = request.FILES.get('school_file4')
                temp_form.save()
            if form.is_valid():
                for i in range(0, school_major4):
                    form = ResumeUniversitySchoolMajor_Form(request.POST, request.FILES)
                    temp_form = form.save(commit=False)
                    temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                    for temp in temp_title:
                        temp_form.resume_university_major = temp
                    # temp_form.resume_university_major = Resume_Title.objects.last()
                    temp_form.resume_university_major_list = request.POST.get('study_major_list4{0}'.format(i))
                    temp_form.resume_university_major_detail = request.POST.get('study_major_detail4{0}'.format(i))
                    temp_form.save()  # 11-22 학과가 제대로 저장안됨 이력서 제목이 여러개 저장되는건지 확인해야함

                ##########################################################################################################
                for i in range(0, out_play):
                    form = ResumeOutPlay(request.POST, request.FILES)
                    temp_form = form.save(commit=False)
                    temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                    for temp in temp_title:
                        temp_form.resume_out_play = temp
                    temp_form.resume_out_activity = request.POST.get('out_play1{0}'.format(i))
                    temp_form.resume_out_place = request.POST.get('out_play2{0}'.format(i))
                    temp_form.resume_out_start_play = request.POST.get('out_play3{0}'.format(i))
                    temp_form.resume_out_end_play = request.POST.get('out_play4{0}'.format(i))
                    temp_form.resume_out_play_text = request.POST.get('out_play5{0}'.format(i))
                    temp_form.save()

                for i in range(0, prize_play):
                    form = ResumePrizePlay(request.POST, request.FILES)
                    temp_form = form.save(commit=False)
                    temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                    for temp in temp_title:
                        temp_form.resume_prize_play = temp
                    temp_form.resume_prize_certificate = request.POST.get('prize_play1{0}'.format(i))
                    temp_form.resume_prize_place = request.POST.get('prize_play2{0}'.format(i))
                    temp_form.resume_prize_title = request.POST.get('prize_play3{0}'.format(i))
                    temp_form.resume_prize_date = request.POST.get('prize_play4{0}'.format(i))
                    temp_form.save()

                for i in range(0, port_polio):
                    form = ResumePortPolio(request.POST, request.FILES)
                    temp_form = form.save(commit=False)
                    temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                    for temp in temp_title:
                        temp_form.resume_port_polio = temp
                    temp_form.resume_port_polio_detail = request.FILES.get('port_polio1{0}'.format(i))
                    temp_form.save()

                for i in range(0, self_introduce):
                    form = ResumeSelfIntroduce(request.POST, request.FILES)
                    temp_form = form.save(commit=False)
                    temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                    for temp in temp_title:
                        temp_form.resume_self_introduce = temp
                    temp_form.resume_self_introduce_title = request.POST.get('self_introduce1{0}'.format(i))
                    temp_form.resume_self_introduce_text = request.POST.get('self_introduce2{0}'.format(i))
                    temp_form.save()

                ##################################################################################################################
        if request.POST.get('resume_submit1'):
            return redirect('resumeapp:resume_resume5', title=title, pk=pk)
        else:
            return redirect('resumeapp:resume_resume4', title=title, career=2, company_ability=1, company_project=0, pk=pk)
        # return render(request, 'resume_resume3.html', context)
        # study_major_list4
        # study_major_detail4

    return render(request, 'resume_resume2.html', context)

def resume_resume2_update(request, school, school_major4, title, pk):
    temp_school_major4 = [[0]]

    context = {}
    context['school'] = school
    context['school_major4'] = school_major4

    context['temp_school_major4'] = temp_school_major4

    context['title'] = title
    context['pk'] = pk
    if request.method == 'POST' and request.POST.get('major_button_plus'):
        school_major4 += 1
        context['school_major4'] = school_major4

    for i in range(1, school_major4):
        temp_school_major4.append([i])
    context['temp_school_major4'] = temp_school_major4

    if request.method == 'POST' and request.POST.get('resume_submit1'):
        print(school)
        resume_title = Resume_Title.objects.filter(pk=title)
        for resume in resume_title:
            find_resume = Resume_ElementarySchool.objects.filter(resume_elementary=resume)
            find_resume.delete()
            find_resume = Resume_MiddleSchool.objects.filter(resume_middle=resume)
            find_resume.delete()
            find_resume = Resume_HighSchool.objects.filter(resume_high=resume)
            find_resume.delete()
            find_resume = Resume_UniversitySchool.objects.filter(resume_university=resume)
            find_resume.delete()
            find_resume = Resume_UniversitySchool_Major.objects.filter(resume_university_major=resume)
            find_resume.delete()
            if school == 1:
                form = ResumeElementaryForm(request.POST, request.FILES)
                if form.is_valid():
                    temp_form = form.save(commit=False)
                    temp_form.resume_elementary = resume
                    if request.POST.get('초졸검정고시') == 'on':
                        temp_form.elementary_school_name = '초졸검정고시'
                        temp_form.elementary_gamjang_time = request.POST['elementary_gamjang_day']
                        temp_form.elementary_state = '졸업'
                        temp_form.elementary_school_file = request.FILES.get('school_file1')
                        temp_form.save()
                    else:
                        temp_form.elementary_school_name = request.POST['elementary_school_name']
                        temp_form.elementary_field_name = request.POST['study_field1']
                        temp_form.elementary_start_time = request.POST['study_start1']
                        temp_form.elementary_end_time = request.POST['study_end1']
                        temp_form.elementary_state = request.POST['elementary_state']
                        temp_form.elementary_school_file = request.FILES.get('school_file1')
                        temp_form.save()
            if school == 2:
                form = ResumeMiddleForm(request.POST, request.FILES)
                if form.is_valid():
                    temp_form = form.save(commit=False)
                    temp_form.resume_middle = resume
                    if request.POST.get('중졸검정고시') == 'on':
                        temp_form.middle_school_name = '중졸검정고시'
                        temp_form.middle_gamjang_time = request.POST['middle_gamjang_day']
                        temp_form.middle_state = '졸업'
                        temp_form.middle_school_file = request.FILES.get('school_file2')
                        temp_form.save()
                    else:
                        temp_form.middle_school_name = request.POST['middle_school_name']
                        temp_form.middle_field_name = request.POST['study_field2']
                        temp_form.middle_start_time = request.POST['study_start2']
                        temp_form.middle_end_time = request.POST['study_end2']
                        temp_form.middle_state = request.POST['middle_state']
                        temp_form.middle_school_file = request.FILES.get('school_file2')
                        temp_form.save()
            if school == 3:
                form = ResumeHighForm(request.POST, request.FILES)
                if form.is_valid():
                    temp_form = form.save(commit=False)
                    temp_form.resume_high = resume
                    if request.POST.get('고졸검정고시') == 'on':
                        temp_form.high_school_name = '고졸검정고시'
                        temp_form.high_gamjang_time = request.POST['high_gamjang_day']
                        temp_form.high_state = '졸업'
                        temp_form.high_school_file = request.FILES.get('school_file3')
                        temp_form.save()
                    else:
                        temp_form.high_school_name = request.POST['high_school_name']
                        temp_form.high_field_name = request.POST['study_field3']
                        temp_form.high_start_time = request.POST['study_start3']
                        temp_form.high_end_time = request.POST['study_end3']
                        temp_form.high_major = request.POST['study_major3']
                        temp_form.high_state = request.POST['high_state']
                        temp_form.high_school_file = request.FILES.get('school_file3')
                        temp_form.save()
            if school == 4:
                form = ResumeUniversityForm(request.POST, request.FILES)
                if form.is_valid():
                    temp_form = form.save(commit=False)
                    temp_form.resume_university = resume
                    temp_form.university_study_year = request.POST['study_year4']
                    temp_form.university_school_name = request.POST['university_school_name']
                    temp_form.university_field_name = request.POST['study_field4']
                    temp_form.university_start_time = request.POST['study_start4']
                    temp_form.university_end_time = request.POST['study_end4']
                    temp_form.university_study_time = request.POST['study_time4']
                    temp_form.university_study_level = request.POST['study_level4']
                    temp_form.university_finaltest = request.POST['study_finaltest4']
                    temp_form.university_school_file = request.FILES.get('school_file4')
                    temp_form.save()
                if form.is_valid():
                    for i in range(0, school_major4):
                        form = ResumeUniversitySchoolMajor_Form(request.POST, request.FILES)
                        temp_form = form.save(commit=False)
                        temp_form.resume_university_major = resume
                        # temp_form.resume_university_major = Resume_Title.objects.last()
                        temp_form.resume_university_major_list = request.POST.get('study_major_list4{0}'.format(i))
                        temp_form.resume_university_major_detail = request.POST.get('study_major_detail4{0}'.format(i))
                        temp_form.save()  # 11-22 학과가 제대로 저장안됨 이력서 제목이 여러개 저장되는건지 확인해야함
        return redirect('resumeapp:detail_resume', title=title)

    return render(request, 'resume_resume2_update.html', context)

def resume_resume3(request, title, pk):
    context={}
    context['pk'] = pk
    context['title'] = title
    return render(request, 'resume_resume3.html', context)

def resume_resume4(request, title, career, company_ability, company_project, pk):
    company_ability_list = []
    company_project_list = []
    # print(company_ability,'111111111111111111111111111111111')
    context = {}
    context['pk'] = pk
    context['title'] = title
    context['career'] = career
    context['company_ability'] = company_ability
    context['company_ability_list'] = company_ability_list
    context['company_project'] = company_project
    context['company_project_list'] = company_project_list

    if request.method == 'POST' and request.POST.get('company_ability_plus'):
        company_ability += 1
        context['company_ability'] = company_ability

    if request.method == 'POST' and request.POST.get('company_project_plus'):
        company_project += 1
        context['company_project'] = company_project

    for i in range(0, company_ability):
        company_ability_list.append([i])
    context['company_ability_list'] = company_ability_list
    for i in range(0, company_project):
        company_project_list.append([i])
    context['company_project_list'] = company_project_list

    if request.method == 'POST' and request.POST.get('resume_submit1'):
        form = ResumeCareerForm(request.POST, request.FILES)
        resume_title = Resume_Title.objects.filter(pk=title)
        if form.is_valid():
            temp_form = form.save(commit=False)
            for temp in resume_title:
                temp_form.resume_career = temp
            temp_form.resume_company_name = request.POST.get('company_name')
            temp_form.resume_career_start_time = request.POST.get('company_start')
            temp_form.resume_career_end_time = request.POST.get('company_end')
            temp_form.resume_career_out = request.POST.get('company_out')
            temp_form.resume_career_position = request.POST.get('accordion1')
            temp_form.resume_career_position_detail = request.POST.get('company_work')
            temp_form.resume_career_money = request.POST.get('company_money')
            temp_form.resume_career_money_detail = request.POST.get('company_money2')
            temp_form.resume_career_position_detail2 = request.POST.get('company_work_detail')
            # print('22222222222222222', request.POST.get('accordion1'), '33333333333333333333333333')

            temp_form.resume_company_file = request.FILES.get('company_file')
            temp_form.save()
        if form.is_valid():
            form = ResumeCareerAbilityForm(request.POST, request.FILES)
            temp_form = form.save(commit=False)
            for temp in resume_title:
                temp_form.resume_career_ability = temp
            temp_form.resume_career_ability_text = request.POST.get('company_work_ability')
            temp_form.save()
        if form.is_valid():
            for i in range(0, company_ability):
                # print(request.POST.get('company_work_ability{0}'.format(i)))
                form = ResumeCareerAbilityForm(request.POST, request.FILES)
                temp_form = form.save(commit=False)
                for temp in resume_title:
                    temp_form.resume_career_ability = temp
                temp_form.resume_career_ability_text = request.POST.get('company_work_ability{0}'.format(i))
                temp_form.save()
        if form.is_valid():
            for i in range(0, company_project):
                # print(request.POST.get('company_work_ability{0}'.format(i)))
                form = ResumeCareerProjectForm(request.POST, request.FILES)
                temp_form = form.save(commit=False)
                for temp in resume_title:
                    temp_form.resume_career_project = temp
                temp_form.resume_career_project_text = request.POST.get('company_project{0}'.format(i))
                temp_form.resume_career_project_start_time = request.POST.get('company_project_start{0}'.format(i))
                temp_form.resume_career_project_end_time = request.POST.get('company_project_end{0}'.format(i))
                temp_form.resume_career_project_text_detail = request.POST.get('company_project_detail{0}'.format(i))
                temp_form.save()
        return redirect('resumeapp:resume_resume5', title=title, pk=pk)

    return render(request, 'resume_resume4.html', context)

def resume_resume4_update(request, company_ability, company_project, title, pk):
    company_ability_list = []
    company_project_list = []

    context = {}
    context['pk'] = pk
    context['title'] = title

    context['company_ability'] = company_ability
    context['company_ability_list'] = company_ability_list
    context['company_project'] = company_project
    context['company_project_list'] = company_project_list

    if request.method == 'POST' and request.POST.get('company_ability_plus'):
        company_ability += 1
        context['company_ability'] = company_ability

    if request.method == 'POST' and request.POST.get('company_project_plus'):
        company_project += 1
        context['company_project'] = company_project

    for i in range(0, company_ability):
        company_ability_list.append([i])
    context['company_ability_list'] = company_ability_list
    for i in range(0, company_project):
        company_project_list.append([i])
    context['company_project_list'] = company_project_list

    if request.method == 'POST' and request.POST.get('resume_submit1'):
        resume_title = Resume_Title.objects.filter(pk=title)
        for resume in resume_title:
            find_resume = Resume_Career.objects.filter(resume_career=resume)
            find_resume.delete()
            find_resume = Resume_Career_Ability.objects.filter(resume_career_ability=resume)
            find_resume.delete()
            find_resume = Resume_Career_Project.objects.filter(resume_career_project=resume)
            find_resume.delete()
            form = ResumeCareerForm(request.POST, request.FILES)
            if form.is_valid():
                temp_form = form.save(commit=False)
                temp_form.resume_career = resume
                temp_form.resume_company_name = request.POST.get('company_name')
                temp_form.resume_career_start_time = request.POST.get('company_start')
                temp_form.resume_career_end_time = request.POST.get('company_end')
                temp_form.resume_career_out = request.POST.get('company_out')
                temp_form.resume_career_position = request.POST.get('accordion1')
                temp_form.resume_career_position_detail = request.POST.get('company_work')
                temp_form.resume_career_money = request.POST.get('company_money')
                temp_form.resume_career_money_detail = request.POST.get('company_money2')
                temp_form.resume_career_position_detail2 = request.POST.get('company_work_detail')
                # print('22222222222222222', request.POST.get('accordion1'), '33333333333333333333333333')

                temp_form.resume_company_file = request.FILES.get('company_file')
                temp_form.save()
            if form.is_valid():
                form = ResumeCareerAbilityForm(request.POST, request.FILES)
                temp_form = form.save(commit=False)
                temp_form.resume_career_ability = resume
                temp_form.resume_career_ability_text = request.POST.get('company_work_ability')
                temp_form.save()
            if form.is_valid():
                for i in range(0, company_ability):
                    form = ResumeCareerAbilityForm(request.POST, request.FILES)
                    temp_form = form.save(commit=False)
                    temp_form.resume_career_ability = resume
                    temp_form.resume_career_ability_text = request.POST.get('company_work_ability{0}'.format(i))
                    temp_form.save()
            if form.is_valid():
                for i in range(0, company_project):
                    form = ResumeCareerProjectForm(request.POST, request.FILES)
                    temp_form = form.save(commit=False)
                    temp_form.resume_career_project = resume
                    temp_form.resume_career_project_text = request.POST.get('company_project{0}'.format(i))
                    temp_form.resume_career_project_start_time = request.POST.get('company_project_start{0}'.format(i))
                    temp_form.resume_career_project_end_time = request.POST.get('company_project_end{0}'.format(i))
                    temp_form.resume_career_project_text_detail = request.POST.get('company_project_detail{0}'.format(i))
                    temp_form.save()
        return redirect('resumeapp:detail_resume', title=title)

    return render(request, 'resume_resume4_update.html', context)

def resume_resume5(request, title, pk):
    if request.method == 'POST' and request.POST.get('resume_submit1'):
        form = ResumeHopeWorkForm(request.POST, request.FILES)
        resume_title = Resume_Title.objects.filter(pk=title)
        print(request.POST)
        field_list = request.POST.getlist('accordion2')
        field_num = len(request.POST.getlist('accordion2'))
        work_list = request.POST.getlist('work2')
        work_num = len(request.POST.getlist('work2'))
        if form.is_valid():
            temp_form = form.save(commit=False)
            for temp in resume_title:
                temp_form.resume_hope_work = temp
            temp_form.resume_hope_work_start_time = request.POST.get('calender_start3')
            temp_form.resume_hope_work_end_time = request.POST.get('calender_end3')
            temp_form.resume_hope_work_money = request.POST.get('company_select_money')
            temp_form.save()
        if form.is_valid():
            for i in range(0, field_num):
                form = ResumeHopeWorkFieldForm(request.POST, request.FILES)
                temp_form = form.save(commit=False)
                for temp in resume_title:
                    temp_form.resume_hope_work_field = temp
                temp_form.resume_hope_work_field1 = field_list[i]
                temp_form.save()
        if form.is_valid():
            for i in range(0, work_num):
                form = ResumeHopeWorkWorkForm(request.POST, request.FILES)
                temp_form = form.save(commit=False)
                for temp in resume_title:
                    temp_form.resume_hope_work_work = temp
                temp_form.resume_hope_work_work1 = work_list[i]
                temp_form.save()
        return redirect('mainapp:main')
    context={}
    context['pk'] = pk
    context['title'] = title
    return render(request, 'resume_resume5.html', context)

def resume_resume5_update(request, title, pk):
    if request.method == 'POST' and request.POST.get('resume_submit1'):
        resume_title = Resume_Title.objects.filter(pk=title)
        for resume in resume_title:
            find_resume = Resume_Hope_Work.objects.filter(resume_hope_work=resume)
            find_resume.delete()
            find_resume = Resume_Hope_Work_Field.objects.filter(resume_hope_work_field=resume)
            find_resume.delete()
            find_resume = Resume_Hope_Work_Work.objects.filter(resume_hope_work_work=resume)
            find_resume.delete()

            form = ResumeHopeWorkForm(request.POST, request.FILES)
            field_list = request.POST.getlist('accordion2')
            field_num = len(request.POST.getlist('accordion2'))
            work_list = request.POST.getlist('work2')
            work_num = len(request.POST.getlist('work2'))
            if form.is_valid():
                temp_form = form.save(commit=False)
                temp_form.resume_hope_work = resume
                temp_form.resume_hope_work_start_time = request.POST.get('calender_start3')
                temp_form.resume_hope_work_end_time = request.POST.get('calender_end3')
                temp_form.resume_hope_work_money = request.POST.get('company_select_money')
                temp_form.save()
            if form.is_valid():
                for i in range(0, field_num):
                    form = ResumeHopeWorkFieldForm(request.POST, request.FILES)
                    temp_form = form.save(commit=False)
                    temp_form.resume_hope_work_field = resume
                    temp_form.resume_hope_work_field1 = field_list[i]
                    temp_form.save()
            if form.is_valid():
                for i in range(0, work_num):
                    form = ResumeHopeWorkWorkForm(request.POST, request.FILES)
                    temp_form = form.save(commit=False)
                    temp_form.resume_hope_work_work = resume
                    temp_form.resume_hope_work_work1 = work_list[i]
                    temp_form.save()
        return redirect('resumeapp:detail_resume', title=title)
    context={}
    context['pk'] = pk
    context['title'] = title
    return render(request, 'resume_resume5_update.html', context)

def resume_out_play_update(request, out_play, title, pk):
    temp_out_play = []

    context = {}
    context['out_play'] = out_play
    context['temp_out_play'] = temp_out_play

    context['pk'] = pk
    context['title'] = title

    if request.method == 'POST' and request.POST.get('out_play_button'):
        out_play += 1
        context['out_play'] = out_play

    for i in range(0, out_play):
        temp_out_play.append([i])

    context['temp_out_play'] = temp_out_play

    if request.method == 'POST' and request.POST.get('resume_submit1'):
        resume_title = Resume_Title.objects.filter(pk=title)
        for resume in resume_title:
            find_resume = Resume_Out_Play.objects.filter(resume_out_play=resume)
            find_resume.delete()
            form = ResumeOutPlay(request.POST, request.FILES)
            if form.is_valid():
                for i in range(0, out_play):
                    form = ResumeOutPlay(request.POST, request.FILES)
                    temp_form = form.save(commit=False)
                    temp_form.resume_out_play = resume
                    temp_form.resume_out_activity = request.POST.get('out_play1{0}'.format(i))
                    temp_form.resume_out_place = request.POST.get('out_play2{0}'.format(i))
                    temp_form.resume_out_start_play = request.POST.get('out_play3{0}'.format(i))
                    temp_form.resume_out_end_play = request.POST.get('out_play4{0}'.format(i))
                    temp_form.resume_out_play_text = request.POST.get('out_play5{0}'.format(i))
                    temp_form.save()
        return redirect('resumeapp:detail_resume', title=title)
    return render(request, 'resume_out_play_update.html', context)

def resume_prize_play_update(request, prize_play, title, pk):
    temp_prize_play = []

    context = {}
    context['prize_play'] = prize_play
    context['temp_prize_play'] = temp_prize_play

    context['pk'] = pk
    context['title'] = title

    if request.method == 'POST' and request.POST.get('prize_play_button'):
        prize_play += 1
        context['prize_play'] = prize_play

    for i in range(0, prize_play):
        temp_prize_play.append([i])

    context['temp_prize_play'] = temp_prize_play

    if request.method == 'POST' and request.POST.get('resume_submit1'):
        resume_title = Resume_Title.objects.filter(pk=title)
        for resume in resume_title:
            find_resume = Resume_Prize_Play.objects.filter(resume_prize_play=resume)
            find_resume.delete()
            form = ResumePrizePlay(request.POST, request.FILES)
            if form.is_valid():
                for i in range(0, prize_play):
                    form = ResumePrizePlay(request.POST, request.FILES)
                    temp_form = form.save(commit=False)
                    temp_form.resume_prize_play = resume
                    temp_form.resume_prize_certificate = request.POST.get('prize_play1{0}'.format(i))
                    temp_form.resume_prize_place = request.POST.get('prize_play2{0}'.format(i))
                    temp_form.resume_prize_title = request.POST.get('prize_play3{0}'.format(i))
                    temp_form.resume_prize_date = request.POST.get('prize_play4{0}'.format(i))
                    temp_form.save()
        return redirect('resumeapp:detail_resume', title=title)
    return render(request, 'resume_prize_play_update.html', context)

def resume_port_polio_update(request, port_polio, title, pk):
    temp_port_polio = []

    context = {}
    context['port_polio'] = port_polio
    context['temp_port_polio'] = temp_port_polio

    context['pk'] = pk
    context['title'] = title

    if request.method == 'POST' and request.POST.get('port_polio_button'):
        port_polio += 1
        context['port_polio'] = port_polio

    for i in range(0, port_polio):
        temp_port_polio.append([i])

    context['temp_port_polio'] = temp_port_polio

    if request.method == 'POST' and request.POST.get('resume_submit1'):
        resume_title = Resume_Title.objects.filter(pk=title)
        for resume in resume_title:
            find_resume = Resume_Port_Polio.objects.filter(resume_port_polio=resume)
            find_resume.delete()
            form = ResumePortPolio(request.POST, request.FILES)
            if form.is_valid():
                for i in range(0, port_polio):
                    form = ResumePortPolio(request.POST, request.FILES)
                    temp_form = form.save(commit=False)
                    temp_form.resume_port_polio = resume
                    temp_form.resume_port_polio_detail = request.FILES.get('port_polio1{0}'.format(i))
                    temp_form.save()
        return redirect('resumeapp:detail_resume', title=title)
    return render(request, 'resume_port_polio_update.html', context)

def resume_self_introduce_update(request, self_introduce, title, pk):
    temp_self_introduce = []

    context = {}
    context['self_introduce'] = self_introduce
    context['temp_self_introduce'] = temp_self_introduce

    context['pk'] = pk
    context['title'] = title

    if request.method == 'POST' and request.POST.get('self_introduce_button'):
        self_introduce += 1
        context['self_introduce'] = self_introduce

    for i in range(0, self_introduce):
        temp_self_introduce.append([i])

    context['temp_self_introduce'] = temp_self_introduce

    if request.method == 'POST' and request.POST.get('resume_submit1'):
        resume_title = Resume_Title.objects.filter(pk=title)
        for resume in resume_title:
            find_resume = Resume_Self_Introduce.objects.filter(resume_self_introduce=resume)
            find_resume.delete()
            form = ResumeSelfIntroduce(request.POST, request.FILES)
            if form.is_valid():
                for i in range(0, self_introduce):
                    form = ResumeSelfIntroduce(request.POST, request.FILES)
                    temp_form = form.save(commit=False)
                    temp_form.resume_self_introduce = resume
                    temp_form.resume_self_introduce_title = request.POST.get('self_introduce1{0}'.format(i))

                    temp_introduce_text = request.POST.get('self_introduce2{0}'.format(i))
                    data = ''
                    for temp_data in temp_introduce_text:
                        if temp_data == ' ':
                            data += '∠'
                        elif temp_data == '\r':
                            data += '∏'
                        else:
                            data += temp_data
                    temp_form.resume_self_introduce_text = data
                    temp_form.save()


        return redirect('resumeapp:detail_resume', title=title)
    return render(request, 'resume_self_introduce_update.html', context)


########################################################################################################################################################

def trash_test(request):
    context={}
    return render(request, 'trash_test.html', context)

def trash_test2(request):
    context={}
    return render(request, 'trash_test2.html', context)

#######################################################################################################################################
# 페이지 하나에 전부 저장 일단 보류
def resume_write(request, school, school_major4, career, out_play, prize_play, port_polio, self_introduce, company_ability, company_project, pk):
    temp_school_major4 = [[0]]
    temp_out_play = []
    temp_prize_play = []
    temp_port_polio = []
    temp_self_introduce = []

    context = {}
    context['school'] = school
    context['school_major4'] = school_major4
    context['career'] = career
    context['out_play'] = out_play
    context['prize_play'] = prize_play
    context['port_polio'] = port_polio
    context['self_introduce'] = self_introduce

    context['temp_school_major4'] = temp_school_major4
    context['temp_out_play'] = temp_out_play
    context['temp_prize_play'] = temp_prize_play
    context['temp_port_polio'] = temp_port_polio
    context['temp_self_introduce'] = temp_self_introduce

    context['company_ability'] = company_ability
    context['company_project'] = company_project

    context['pk'] = pk
    if request.method == 'POST' and request.POST.get('major_button_plus'):
        school_major4 += 1
        context['school_major4'] = school_major4

    if request.method == 'POST' and request.POST.get('out_play_button'):
        out_play += 1
        context['out_play'] = out_play

    if request.method == 'POST' and request.POST.get('prize_play_button'):
        prize_play += 1
        context['prize_play'] = prize_play

    if request.method == 'POST' and request.POST.get('port_polio_button'):
        port_polio += 1
        context['port_polio'] = port_polio

    if request.method == 'POST' and request.POST.get('self_introduce_button'):
        self_introduce += 1
        context['self_introduce'] = self_introduce

    for i in range(1, school_major4):
        temp_school_major4.append([i])
    for i in range(0, out_play):
        temp_out_play.append([i])
    for i in range(0, prize_play):
        temp_prize_play.append([i])
    for i in range(0, port_polio):
        temp_port_polio.append([i])
    for i in range(0, self_introduce):
        temp_self_introduce.append([i])
    context['temp_school_major4'] = temp_school_major4
    context['temp_out_play'] = temp_out_play
    context['temp_prize_play'] = temp_prize_play
    context['temp_port_polio'] = temp_port_polio
    context['temp_self_introduce'] = temp_self_introduce

    if request.method == 'POST' and request.POST.get('resume_submit1'):
        print('*******************************', request.POST, '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
        temp_user = MyUser.objects.filter(pk=pk)
        form = ResumeTitleForm(request.POST, request.FILES)
        if form.is_valid():
            temp_form = form.save(commit=False)
            for temp in temp_user:
                temp_form.resume_title = temp
            temp_form.resume_title_detail = request.POST['resume_title']
            temp_form.save()
        if request.method == 'POST' and school == 1:
            form = ResumeElementaryForm(request.POST, request.FILES)
            if form.is_valid():
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    title = temp.pk
                    temp_form.resume_elementary = temp
                temp_form.elementary_school_name = request.POST['elementary_school_name']
                temp_form.elementary_field_name = request.POST['study_field1']
                temp_form.elementary_start_time = request.POST['study_start1']
                temp_form.elementary_end_time = request.POST['study_end1']
                temp_form.save()

            for i in range(0, out_play):
                form = ResumeOutPlay(request.POST, request.FILES)
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    temp_form.resume_out_play = temp
                temp_form.resume_out_activity = request.POST.get('out_play1{0}'.format(i))
                temp_form.resume_out_place = request.POST.get('out_play2{0}'.format(i))
                temp_form.resume_out_start_play = request.POST.get('out_play3{0}'.format(i))
                temp_form.resume_out_end_play = request.POST.get('out_play4{0}'.format(i))
                temp_form.resume_out_play_text = request.POST.get('out_play5{0}'.format(i))
                temp_form.save()

            for i in range(0, prize_play):
                form = ResumePrizePlay(request.POST, request.FILES)
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    temp_form.resume_prize_play = temp
                temp_form.resume_prize_certificate = request.POST.get('prize_play1{0}'.format(i))
                temp_form.resume_prize_place = request.POST.get('prize_play2{0}'.format(i))
                temp_form.resume_prize_title = request.POST.get('prize_play3{0}'.format(i))
                temp_form.resume_prize_date = request.POST.get('prize_play4{0}'.format(i))
                temp_form.save()

            for i in range(0, port_polio):
                form = ResumePortPolio(request.POST, request.FILES)
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    temp_form.resume_port_polio = temp
                temp_form.resume_port_polio_detail = request.FILES.get('port_polio1{0}'.format(i))
                temp_form.save()

            for i in range(0, self_introduce):
                form = ResumeSelfIntroduce(request.POST, request.FILES)
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    temp_form.resume_self_introduce = temp
                temp_form.resume_self_introduce_title = request.POST.get('self_introduce1{0}'.format(i))
                temp_form.resume_self_introduce_text = request.POST.get('self_introduce2{0}'.format(i))
                temp_form.save()
        elif request.method == 'POST' and school == 2:
            form = ResumeMiddleForm(request.POST, request.FILES)
            if form.is_valid():
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    title = temp.pk
                    temp_form.resume_middle = temp
                temp_form.middle_school_name = request.POST['middle_school_name']
                temp_form.middle_field_name = request.POST['study_field2']
                temp_form.middle_start_time = request.POST['study_start2']
                temp_form.middle_end_time = request.POST['study_end2']
                temp_form.save()

            for i in range(0, out_play):
                form = ResumeOutPlay(request.POST, request.FILES)
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    temp_form.resume_out_play = temp
                temp_form.resume_out_activity = request.POST.get('out_play1{0}'.format(i))
                temp_form.resume_out_place = request.POST.get('out_play2{0}'.format(i))
                temp_form.resume_out_start_play = request.POST.get('out_play3{0}'.format(i))
                temp_form.resume_out_end_play = request.POST.get('out_play4{0}'.format(i))
                temp_form.resume_out_play_text = request.POST.get('out_play5{0}'.format(i))
                temp_form.save()

            for i in range(0, prize_play):
                form = ResumePrizePlay(request.POST, request.FILES)
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    temp_form.resume_prize_play = temp
                temp_form.resume_prize_certificate = request.POST.get('prize_play1{0}'.format(i))
                temp_form.resume_prize_place = request.POST.get('prize_play2{0}'.format(i))
                temp_form.resume_prize_title = request.POST.get('prize_play3{0}'.format(i))
                temp_form.resume_prize_date = request.POST.get('prize_play4{0}'.format(i))
                temp_form.save()

            for i in range(0, port_polio):
                form = ResumePortPolio(request.POST, request.FILES)
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    temp_form.resume_port_polio = temp
                temp_form.resume_port_polio_detail = request.FILES.get('port_polio1{0}'.format(i))
                temp_form.save()

            for i in range(0, self_introduce):
                form = ResumeSelfIntroduce(request.POST, request.FILES)
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    temp_form.resume_self_introduce = temp
                temp_form.resume_self_introduce_title = request.POST.get('self_introduce1{0}'.format(i))
                temp_form.resume_self_introduce_text = request.POST.get('self_introduce2{0}'.format(i))
                temp_form.save()
        elif request.method == 'POST' and school == 3:
            form = ResumeHighForm(request.POST, request.FILES)
            if form.is_valid():
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    title = temp.pk
                    temp_form.resume_high = temp
                temp_form.high_school_name = request.POST['high_school_name']
                temp_form.high_field_name = request.POST['study_field3']
                temp_form.high_start_time = request.POST['study_start3']
                temp_form.high_end_time = request.POST['study_end3']
                temp_form.high_major = request.POST['study_major3']
                temp_form.save()

            for i in range(0, out_play):
                form = ResumeOutPlay(request.POST, request.FILES)
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    temp_form.resume_out_play = temp
                temp_form.resume_out_activity = request.POST.get('out_play1{0}'.format(i))
                temp_form.resume_out_place = request.POST.get('out_play2{0}'.format(i))
                temp_form.resume_out_start_play = request.POST.get('out_play3{0}'.format(i))
                temp_form.resume_out_end_play = request.POST.get('out_play4{0}'.format(i))
                temp_form.resume_out_play_text = request.POST.get('out_play5{0}'.format(i))
                temp_form.save()

            for i in range(0, prize_play):
                form = ResumePrizePlay(request.POST, request.FILES)
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    temp_form.resume_prize_play = temp
                temp_form.resume_prize_certificate = request.POST.get('prize_play1{0}'.format(i))
                temp_form.resume_prize_place = request.POST.get('prize_play2{0}'.format(i))
                temp_form.resume_prize_title = request.POST.get('prize_play3{0}'.format(i))
                temp_form.resume_prize_date = request.POST.get('prize_play4{0}'.format(i))
                temp_form.save()

            for i in range(0, port_polio):
                form = ResumePortPolio(request.POST, request.FILES)
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    temp_form.resume_port_polio = temp
                temp_form.resume_port_polio_detail = request.FILES.get('port_polio1{0}'.format(i))
                temp_form.save()

            for i in range(0, self_introduce):
                form = ResumeSelfIntroduce(request.POST, request.FILES)
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    temp_form.resume_self_introduce = temp
                temp_form.resume_self_introduce_title = request.POST.get('self_introduce1{0}'.format(i))
                temp_form.resume_self_introduce_text = request.POST.get('self_introduce2{0}'.format(i))
                temp_form.save()
        elif request.method == 'POST' and school == 4:
            form = ResumeUniversityForm(request.POST, request.FILES)
            if form.is_valid():
                temp_form = form.save(commit=False)
                temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                for temp in temp_title:
                    title = temp.pk
                    temp_form.resume_university = temp
                temp_form.university_study_year = request.POST['study_year4']
                temp_form.university_school_name = request.POST['university_school_name']
                temp_form.university_field_name = request.POST['study_field4']
                temp_form.university_start_time = request.POST['study_start4']
                temp_form.university_end_time = request.POST['study_end4']
                temp_form.university_study_time = request.POST['study_time4']
                temp_form.university_study_level = request.POST['study_level4']
                temp_form.university_finaltest = request.POST['study_finaltest4']
                temp_form.save()
            if form.is_valid():
                for i in range(0, school_major4):
                    form = ResumeUniversitySchoolMajor_Form(request.POST, request.FILES)
                    temp_form = form.save(commit=False)
                    temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                    for temp in temp_title:
                        temp_form.resume_university_major = temp
                    # temp_form.resume_university_major = Resume_Title.objects.last()
                    temp_form.resume_university_major_list = request.POST.get('study_major_list4{0}'.format(i))
                    temp_form.resume_university_major_detail = request.POST.get('study_major_detail4{0}'.format(i))
                    temp_form.save()  # 11-22 학과가 제대로 저장안됨 이력서 제목이 여러개 저장되는건지 확인해야함

                ##########################################################################################################
                for i in range(0, out_play):
                    form = ResumeOutPlay(request.POST, request.FILES)
                    temp_form = form.save(commit=False)
                    temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                    for temp in temp_title:
                        temp_form.resume_out_play = temp
                    temp_form.resume_out_activity = request.POST.get('out_play1{0}'.format(i))
                    temp_form.resume_out_place = request.POST.get('out_play2{0}'.format(i))
                    temp_form.resume_out_start_play = request.POST.get('out_play3{0}'.format(i))
                    temp_form.resume_out_end_play = request.POST.get('out_play4{0}'.format(i))
                    temp_form.resume_out_play_text = request.POST.get('out_play5{0}'.format(i))
                    temp_form.save()

                for i in range(0, prize_play):
                    form = ResumePrizePlay(request.POST, request.FILES)
                    temp_form = form.save(commit=False)
                    temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                    for temp in temp_title:
                        temp_form.resume_prize_play = temp
                    temp_form.resume_prize_certificate = request.POST.get('prize_play1{0}'.format(i))
                    temp_form.resume_prize_place = request.POST.get('prize_play2{0}'.format(i))
                    temp_form.resume_prize_title = request.POST.get('prize_play3{0}'.format(i))
                    temp_form.resume_prize_date = request.POST.get('prize_play4{0}'.format(i))
                    temp_form.save()

                for i in range(0, port_polio):
                    form = ResumePortPolio(request.POST, request.FILES)
                    temp_form = form.save(commit=False)
                    temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                    for temp in temp_title:
                        temp_form.resume_port_polio = temp
                    temp_form.resume_port_polio_detail = request.FILES.get('port_polio1{0}'.format(i))
                    temp_form.save()

                for i in range(0, self_introduce):
                    form = ResumeSelfIntroduce(request.POST, request.FILES)
                    temp_form = form.save(commit=False)
                    temp_title = Resume_Title.objects.filter(resume_title_detail=request.POST['resume_title'])
                    for temp in temp_title:
                        temp_form.resume_self_introduce = temp
                    temp_form.resume_self_introduce_title = request.POST.get('self_introduce1{0}'.format(i))
                    temp_form.resume_self_introduce_text = request.POST.get('self_introduce2{0}'.format(i))
                    temp_form.save()

                ##################################################################################################################
        return redirect('resumeapp:resume_resume3', title=title, pk=pk)
        # return render(request, 'resume_resume3.html', context)
        # study_major_list4
        # study_major_detail4

    return render(request, 'resume_write.html', context)
