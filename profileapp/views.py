
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
    return render(request, 'create_resume.html', context)

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