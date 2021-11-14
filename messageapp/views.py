from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import DetailView

from accountapp.models import MyUser
from friendapp.models import FriendRequestModel


def friend_request_message(request, pk):
    if request.user.pk == pk:
        context = {}
        friend_request_message = FriendRequestModel.objects.filter(B_User=request.user)
        context['friend_request_message'] = friend_request_message
        return render(request, 'message_box.html', context)
    else:
        raise Http404("잘못된 접근입니다")

def delete_message(request, pk):
    request_friend_data = FriendRequestModel.objects.filter(pk=pk)
    for request_friend_delete in request_friend_data:
        temp_pk = request_friend_delete.B_User.pk
        request_friend_delete.delete()
    return redirect('messageapp:message_box', temp_pk)


