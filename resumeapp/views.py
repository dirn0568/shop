from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from accountapp.models import MyUser
from resumeapp.forms import ResumeForm, Update_ResumeForm
from resumeapp.models import User_Resume


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

def test_resume(request, test ,pk):
    test_list = [0]
    if request.method == "GET":
        test = 0
    if request.method == "POST":
        test += 1
        for i in range(test):
            test_list.append([0])

    context={}
    context['pk'] = pk
    print(test_list)
    context['test_list'] = test_list
    context['test_resume'] = test
    return render(request, 'test_resume.html', context)