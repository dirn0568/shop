from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

from accountapp.models import MyUser, Friend_List
from django.http import request
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import Update_User_Form, Create_User_Form, Create_Company_User_Form
from friendapp.models import FriendRequestModel
from profileapp.models import User_Profile
from resumeapp.models import User_Resume, Resume_Title


class Create_User(CreateView):
    model = MyUser
    form_class = Create_User_Form
    template_name = 'create_user.html'

    def get_success_url(self):
        return reverse('accountapp:login')

class Detail_User(DetailView):
    model = MyUser
    context_object_name = 'target_user'
    template_name = 'detail_user.html'

    def get_context_data(self, **kwargs):
        context = super(Detail_User, self).get_context_data(**kwargs)
        temp_user = MyUser.objects.filter(pk=self.object.pk)
        for temp in temp_user:
            user = temp
        temp_profile = User_Profile.objects.filter(profile=user)
        if temp_profile.count() != 0:
            for temp in temp_profile:
                profile = temp
        else:
            profile = None
        temp_resume = Resume_Title.objects.filter(resume_title=user)
        resume_num = 0
        if temp_resume.count() != 0:
            for temp in temp_resume:
                resume_num += 1
        else:
            resume_num = 0
        context['profile'] = profile
        context['resume_num'] = resume_num
        return context


class Update_User(UpdateView):
    model = MyUser
    form_class = Update_User_Form
    context_object_name = 'target_user'
    template_name = 'update_user.html'

    def get_success_url(self):
        return reverse('accountapp:detail_user', kwargs={'pk': self.object.pk})


class Delete_User(DeleteView):
    model = MyUser
    context_object_name = 'target_user'
    template_name = 'delete_user.html'
    success_url = reverse_lazy('mainapp:main')

class Create_Company_User(CreateView):
    model = MyUser
    form_class = Create_Company_User_Form
    template_name = 'create_company_user.html'

    def form_valid(self, form):
        temp_form = form.save(commit=False)
        temp_form.company_group = self.request.POST['company_group']
        # temp_article.article_project = ProjectCreateModel.objects.get(pk=self.request.pk)
        temp_form.company_number = self.request.POST['company_num']
        temp_form.company_name = self.request.POST['company_name']
        temp_form.company_ceo = self.request.POST['company_ceo']
        temp_form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountapp:login')

# class Company_Login_View(LoginView):
#     model = MyUser
#     form_class =

def createfriend(request, friend1, friend2, pk):
    friend_data1 = MyUser.objects.filter(username=friend1)
    friend_data2 = MyUser.objects.filter(username=friend2)
    for data1 in friend_data1:
        for data2 in friend_data2:
            Friend_List(friend=data1, friend_relation=data2).save()
            Friend_List(friend=data2, friend_relation=data1).save()
    request_friend_data = FriendRequestModel.objects.filter(pk=pk)
    for request_friend_delete in request_friend_data:
        temp_pk = request_friend_delete.B_User.pk
        request_friend_delete.delete()
    return redirect('messageapp:message_box', temp_pk)


