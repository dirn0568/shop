from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import DetailView

from accountapp.models import MyUser
from friendapp.models import FriendRequestModel
from messageapp.models import Message_Resume_Model, Test_Data, Message_Send_Model, Message_Propose_Model
from profileapp.models import User_Profile

from datetime import datetime


def message_content(request, pk):
    context={}

    page = request.GET.get('page', '1')

    user = MyUser.objects.filter(pk=pk)
    for temp_user in user:
        message = Message_Send_Model.objects.filter(message_send_receive=temp_user).order_by('-message_send_date_time')
        count = len(message)
    paginator = Paginator(message, 8)

    page_obj = paginator.get_page(page)

    context['message'] = page_obj
    context['count'] = count
    context['pk'] = pk

    return render(request, 'message_content.html', context)

def message_send(request, pk):
    context = {}

    page = request.GET.get('page', '1')

    user = MyUser.objects.filter(pk=pk)
    for temp_user in user:
        message = Message_Send_Model.objects.filter(message_send_send=temp_user).order_by(
            '-message_send_date_time')
        count = len(message)

    paginator = Paginator(message, 8)

    page_obj = paginator.get_page(page)

    context['message'] = page_obj
    context['count'] = count
    context['pk'] = pk
    return render(request, 'message_send.html', context)

def message_write(request, pk):
    context={}

    if request.method == 'POST' and request.POST.get('message_submit1'):
        print(request.POST)
        print('33333333333333333')
        print(request.FILES)

        user = MyUser.objects.filter(username=request.POST.get('receiver'))

        for temp_user in user:
            message = Message_Send_Model(message_send_receive=temp_user, message_send_send=request.user, message_send_title=request.POST.get('title'), message_send_detail=request.POST.get('context'), message_send_file=request.FILES.get('file'))
            message.save()

    context['pk'] = pk
    return render(request, 'message_write.html', context)

def message_search(request, pk):
    context = {}

    page = request.GET.get('page', '1')

    user = MyUser.objects.filter(pk=pk)
    for temp_user in user:
        message = Message_Resume_Model.objects.filter(message_resume_receive=temp_user).order_by('-message_date_time')
        count = len(message)

    paginator = Paginator(message, 8)

    page_obj = paginator.get_page(page)

    context['message'] = page_obj
    context['count'] = count
    context['pk'] = pk

    return render(request, 'message_search.html', context)

def message_propose(request, pk):
    context = {}

    page = request.GET.get('page', '1')

    user = MyUser.objects.filter(pk=pk)
    for temp_user in user:
        message = Message_Propose_Model.objects.filter(message_propose_receive=temp_user).order_by('-message_propose_date_time')
        count = len(message)

    paginator = Paginator(message, 8)

    page_obj = paginator.get_page(page)

    context['message'] = page_obj
    context['count'] = count
    context['pk'] = pk

    return render(request, 'message_propose.html', context)

def message_send_detail(request, title, pk):
    context = {}

    message = Message_Send_Model.objects.filter(pk=title)
    data = ''
    for temp in message:
        context['receive'] = temp.message_send_receive
        context['title'] = temp.message_send_title
        for temp_data in temp.message_send_detail:
            if temp_data == ' ':
                data += '∠'
            elif temp_data == '\r':
                data += '∏'
            else:
                data += temp_data
        context['detail'] = data
        print(data)
        context['file'] = temp.message_send_file
    context['pk'] = pk
    return render(request, 'message_send_detail.html', context)

def message_content_detail(request, title, pk):
    context = {}

    message = Message_Send_Model.objects.filter(pk=title)
    data = ''
    for temp in message:
        context['send'] = temp.message_send_send
        context['title'] = temp.message_send_title
        for temp_data in temp.message_send_detail:
            if temp_data == ' ':
                data += '∠'
            elif temp_data == '\r':
                data += '∏'
            else:
                data += temp_data
        context['detail'] = data
        print(data)
        context['file'] = temp.message_send_file
    context['pk'] = pk
    return render(request, 'message_content_detail.html', context)

def message_propose_detail(request, title, pk):
    context = {}

    detail = request.GET.get('detail', None)
    detail2 = request.GET.get('detail2', None)

    # report = request.GET.get('report', None)

    message = Message_Propose_Model.objects.filter(pk=title)

    if detail != None:
        print('워크래프트31515135134124')
        temp_user = MyUser.objects.filter(pk=request.user.pk)
        for temp in temp_user:
            temp_profile = User_Profile.objects.filter(profile=temp)
        if temp_profile:
            for temp in temp_profile:
                if temp.user_name:
                    message_name = temp.user_name
                else:
                    message_name = "None"
                if temp.user_gender:
                    message_gender = temp.user_gender
                else:
                    message_gender = "None"
                if temp.phone_number:
                    message_phone_number = temp.phone_number
                else:
                    message_phone_number = "None"
                if temp.user_email:
                    message_user_email = temp.user_email
                else:
                    message_user_email = "None"
                if temp.user_birthday:
                    now = datetime.now()
                    date = now.strftime("%Y")
                    date2 = temp.user_birthday[:4]
                    date3 = int(date) - int(date2)

                    date4 = now.strftime("%m")
                    date5 = now.strftime("%d")
                    date6 = temp.user_birthday[4:6]
                    date7 = temp.user_birthday[6:9]
                    date4 = int(date4)
                    date5 = int(date5)
                    date6 = int(date6)
                    date7 = int(date7)
                    if date4 > date6:
                        pass
                    elif date4 == date6 and date5 >= date7:
                        pass
                    else:
                        date3 = date3 - 1
                    print(date3, '마인크래프트#$@%@$@@$')
                    print(temp.user_birthday[:4], '스타크래프트#$@%@@$@%@$')
                    message_age = date3
                else:
                    message_age = "None"
        else:
            message_name = "None"
            message_gender = "None"
            message_phone_number = "None"
            message_user_email = "None"
            message_age = "None"

        for temp in message:
            model = Message_Send_Model(message_send_receive=temp.message_propose_send,
                                       message_send_send=request.user,
                                       message_send_title='면접에 동의하셨습니다',
                                       message_send_detail='"{3}"를 작성하신 {0}님께서 면접에 동의하셨습니다. ∏이름: {4} ∏나이: {5} ∏성별: {6} ∏핸드폰 번호: {1} ∏이메일: {2}'.format(
                                           request.user, message_phone_number, message_user_email, temp.message_propose_resume_title, message_name, message_age, message_gender))
            model.save()

    if detail2 != None:
        print('실행하고 있나요2 05-08')
        for temp in message:
            model = Message_Send_Model(message_send_receive=temp.message_propose_send,
                                       message_send_send=request.user,
                                       message_send_title='면접에 거절하셨습니다',
                                       message_send_detail='"{1}"를 작성하신 {0}님 께서 면접을 거절하셨습니다.'.format(request.user, temp.message_propose_resume_title))
            model.save()

    # if report != None:
    #     print('0603 테스트중')
    #     for temp in message:
    #         print(temp.message_propose_send, temp.message_propose_send.pk)
    #         temp_user = MyUser.objects.filter(username=temp.message_propose_send)
    #         for temp2 in temp_user:
    #             temp2.sos_report += 1
    #             temp2.save()


    data = ''
    for temp in message:
        context['receive'] = temp.message_propose_receive
        context['send'] = temp.message_propose_send
        # context['title'] = temp.message_send_title
        for temp_data in temp.message_propose_detail:
            if temp_data == ' ':
                data += '∠'
            elif temp_data == '\r':
                data += '∏'
            else:
                data += temp_data
        context['detail'] = data
        print(data)
        # context['file'] = temp.message_send_file
        context['company_group'] = temp.message_propose_company_group
        context['company_name'] = temp.message_propose_company_name
        context['company_ceo'] = temp.message_propose_company_ceo
        context['company_logo'] = temp.message_propose_company_logo
        context['company_phone_number'] = temp.message_propose_company_phone_number

        context['message_propose_resume_title'] = temp.message_propose_resume_title
    context['title'] = title
    context['pk'] = pk
    for temp in message:
        temp_user = MyUser.objects.filter(username=temp.message_propose_send)
        for temp2 in temp_user:
            temp_user_pk = temp2.pk

    context['temp_user_pk'] = temp_user_pk
    return render(request, 'message_propose_detail.html', context)

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


