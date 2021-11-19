from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from accountapp.models import MyUser
from resumeapp.forms import ResumeForm, Update_ResumeForm, ResumeElementaryForm
from resumeapp.models import User_Resume, User_Resume_Certificate


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

def test_resume2(request, pk):
    # 테스트 버전2
    context={}
    context['test_form'] = ResumeElementaryForm
    context['pk'] = pk

    return render(request, 'test_resume2.html', context)

def test_calender(request):
    context={}
    return render(request, 'test_calender.html', context)

def test_test(request):
    context={}
    return render(request, 'test_test.html', context)


