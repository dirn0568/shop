from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView

from accountapp.models import MyUser, Friend_List
from friendapp.models import FriendRequestModel

def createfriendview(request, word1, word2):
    friend1 = MyUser.objects.filter(username=word1)
    friend2 = MyUser.objects.filter(username=word2)
    for friend_list in friend1:
        for friend_list2 in friend2:
            FriendRequestModel(A_User=friend_list, B_User=friend_list2).save()
    return redirect('mainapp:main')

def detailfriendview(request, pk):
    if request.user.pk == pk:
        User_pk = MyUser.objects.filter(pk=pk)
        for user_data in User_pk:
            friend_list = Friend_List.objects.filter(friend=user_data)
        context = {}
        context['friend_list'] = friend_list
        return render(request, 'friend_list.html', context)
    else:
        raise Http404("잘못된 접근입니다")

def deletefriendview(request, user, user_friend):
    delete_friend1 = MyUser.objects.filter(username=user)
    delete_friend2 = MyUser.objects.filter(username=user_friend)
    for delete1 in delete_friend1:
        for delete2 in delete_friend2:
            temp_pk = delete1.pk
            delete_friend3 = Friend_List.objects.filter(friend=delete1, friend_relation=delete2)
            delete_friend4 = Friend_List.objects.filter(friend=delete2, friend_relation=delete1)
    for delete3 in delete_friend3:
        for delete4 in delete_friend4:
            delete3.delete()
            delete4.delete()
    return redirect('friendapp:friend_list', temp_pk)



