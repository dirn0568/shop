from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import DetailView

from accountapp.models import MyUser
from friendapp.models import FriendRequestModel
from messageapp.models import Message_Resume_Model, Test_Data


def message_content(request, pk):
    context={}

    page = request.GET.get('page', '1')

    user = MyUser.objects.filter(pk=pk)
    for temp_user in user:
        message = Message_Resume_Model.objects.filter(message_resume_receive=temp_user).order_by('-message_date')

    paginator = Paginator(message, 10)

    page_obj = paginator.get_page(page)

    context['message'] = page_obj

    return render(request, 'message_content.html', context)

def test(request):
    context = {}
    # print(request)

    # for i in range(500):
    #     q = Message_Resume_Model(message_resume_receive=MyUser.objects.first(), message_resume_send=MyUser.objects.last(), message_detail='테스트 데이터입니다:[%03d]' % i)
    #     q.save()

    page = request.GET.get('page', '1')  # 페이지 ??
    # print(page)
    question_list = Test_Data.objects.all()

    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    # print(paginator, '###############')
    page_obj = paginator.get_page(page)
    # print(page_obj)

    context = {'question_list': page_obj}

    return render(request, 'message_test.html', context)

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


