from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from accountapp.models import MyUser
from resumeapp.forms import ResumeForm, Update_ResumeForm, ResumeElementaryForm, ResumeMiddleForm, ResumeHighForm, \
    ResumeUniversityForm, ResumeUniversitySchoolMajor_Form, ResumeTitleForm
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

def resume_1(request, school, pk):
    # 테스트 버전2
    context = {}
    context['school'] = school
    context['pk'] = pk

    if request.method == 'POST':
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
            print('##################################', request.POST, '#######################################################')
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
            form = ResumeUniversitySchoolMajor_Form(request.POST, request.FILES)
            if form.is_valid():
                temp_form = form.save(commit=False)
                temp_form.resume_university_major = Resume_Title.objects.last()
                temp_form.resume_university_major_list = request.POST['study_major_list4']
                temp_form.resume_university_major_detail = request.POST['study_major_detail4']
                temp_form.save()
            # study_major_list4
            # study_major_detail4

    return render(request, 'resume_1.html', context)

def test_test(request):
    if request.method == "POST":
        print(request.POST)
    context={}
    return render(request, 'test_test.html', context)


