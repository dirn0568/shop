from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from accountapp.models import MyUser
from resumeapp.forms import ResumeForm, Update_ResumeForm, ResumeElementaryForm, ResumeMiddleForm, ResumeHighForm, \
    ResumeUniversityForm, ResumeUniversitySchoolMajor_Form, ResumeTitleForm, ResumeCareerForm, ResumeCareerAbilityForm, \
    ResumeCareerProjectForm, ResumeOutPlay, ResumePrizePlay, ResumePortPolio, ResumeSelfIntroduce
from resumeapp.models import User_Resume, User_Resume_Certificate, Resume_Title


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

def list_resume(request, pk):
    temp_user = MyUser.objects.filter(pk=pk)
    for user_test in temp_user:
        if request.user == user_test:
            pass
        else:
            raise Http404("잘못된 접근입니다")
        for temp in temp_user:
            temp_resume = User_Resume.objects.filter(resume=temp)
        context = {}
        context['pk'] = pk
        context['resume'] = temp_resume
    return render(request, 'list_resume.html', context)

def detail_resume(request, pk1, pk2):
    temp_resume = User_Resume.objects.filter(pk=pk2)
    for user_resume in temp_resume:
        if request.user.pk == pk1:
            pass
        else:
            raise Http404("잘못된 접근입니다")
        context = {}
        context['pk1'] = pk1
        context['pk2'] = pk2
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

    return render(request, 'resume_resume2.html', context)

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

def resume_resume5(request, title, pk):
    if request.method == 'POST':
        print(request.POST)
    context={}
    context['pk'] = pk
    context['title'] = title
    return render(request, 'resume_resume5.html', context)

##########################################################################

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
