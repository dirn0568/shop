
from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from accountapp.models import MyUser
from profileapp.forms import ProfileForm, Update_ProfileForm
from profileapp.models import User_Profile


def create_profile(request, pk):
    temp_user = MyUser.objects.filter(pk=pk)
    for user_test in temp_user:
        if request.user == user_test:
            pass
        else:
            raise Http404("잘못된 접근입니다")
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            temp_form = form.save(commit=False)
            for temp in temp_user:
                temp_form.profile = temp
            temp_form.save()
            return redirect('accountapp:detail_user', pk)
    context = {}
    context['profile_form'] = ProfileForm
    context['pk'] = pk
    return render(request, 'create_profile.html', context)

def update_profile(request, pk):
    temp_user = MyUser.objects.filter(pk=pk)
    for user_test in temp_user:
        if request.user == user_test:
            pass
        else:
            raise Http404("잘못된 접근입니다")
    if request.method == "POST":
        form = Update_ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            for temp in temp_user:
                temp_profile = User_Profile.objects.filter(profile=temp)
            for temp in temp_profile:
                if len(request.POST['profile_text']) != 0:
                    temp.profile_text = request.POST['profile_text']
                if request.FILES:
                    temp.profile_img = request.FILES['profile_img']
                temp.save()
            return redirect('accountapp:detail_user', pk)
    context = {}
    context['profile_form'] = Update_ProfileForm
    context['pk'] = pk
    return render(request, 'update_profile.html', context)

def delete_profile(request, pk):
    temp_user = MyUser.objects.filter(pk=pk)
    for user_test in temp_user:
        if request.user == user_test:
            pass
        else:
            raise Http404("잘못된 접근입니다")
    if request.method == "POST":
        for temp in temp_user:
            temp_profile = User_Profile.objects.filter(profile=temp)
        for temp in temp_profile:
            temp.delete()
        return redirect('accountapp:detail_user', pk)
    context = {}
    context['pk'] = pk
    return render(request, 'delete_profile.html', context)


def detail_user_update(request, pk):
    if request.method == "POST" and request.POST.get('resume_submit3'):
        user = MyUser.objects.filter(pk=pk)
        for temp_user in user:
            profile = User_Profile.objects.filter(profile=temp_user)
            if profile:
                for temp_profile in profile:
                    temp_profile.profile_img = None
                    temp_profile.save()
            else:
                pass

    if request.method == "POST" and request.POST.get('resume_submit2'):
        user = MyUser.objects.filter(pk=pk)
        print(request.FILES, '##############################')
        for temp_user in user:
            profile = User_Profile.objects.filter(profile=temp_user)
            if profile:
                for temp_profile in profile:
                    temp_profile.profile_img = request.FILES.get('file')
                    temp_profile.save()
            else:
                form = ProfileForm(request.POST, request.FILES)
                if form.is_valid():
                    temp_form = form.save(commit=False)
                    for temp_user in user:
                        temp_form.profile = temp_user
                    temp_form.profile_img = request.FILES.get('file')
                    temp_form.save()


    if request.method == "POST" and request.POST.get('resume_submit1'):
        user = MyUser.objects.filter(pk=pk)
        print(request.POST, '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        for temp_user in user:
            profile = User_Profile.objects.filter(profile=temp_user)
            if profile:
                for temp_profile in profile:
                    temp_profile.user_name = request.POST.get('user_name')
                    temp_profile.user_birthday = request.POST.get('user_birthday')
                    temp_profile.user_gender = request.POST.get('gender')
                    temp_profile.phone_number = request.POST.get('user_number')
                    temp_profile.user_email = request.POST.get('user_email')
                    temp_profile.user_page = request.POST.get('user_page')
                    temp_profile.save()
            else:
                form = ProfileForm(request.POST, request.FILES)
                if form.is_valid():
                    print('실행중?2222222222222222222222')
                    temp_form = form.save(commit=False)
                    for temp_user in user:
                        temp_form.profile = temp_user
                    temp_form.user_name = request.POST.get('user_name')
                    temp_form.user_birthday = request.POST.get('user_birthday')
                    temp_form.user_gender = request.POST.get('gender')
                    temp_form.phone_number = request.POST.get('user_number')
                    temp_form.user_email = request.POST.get('user_email')
                    temp_form.user_page = request.POST.get('user_page')
                    temp_form.save()

    return redirect('accountapp:detail_user', pk=pk)
