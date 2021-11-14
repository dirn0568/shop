import os

from django.shortcuts import render

from accountapp.models import MyUser
from chatapp.forms import ChatForm
from chatapp.models import ChatModel


def chatview(request, pk):
    if request.method == "POST":
        form = ChatForm(request.POST, request.FILES)
        if form.is_valid():
            temp_form = form.save(commit=False)
            test_temp = str(temp_form.chat_img)
            name, ext = os.path.splitext(test_temp)
            temp_form.chat_img_ext = ext
            temp_form.send_user = request.user
            receive = MyUser.objects.filter(pk=pk)
            for list in receive:
                temp_form.receive_user = list
            temp_form.save()
    context = {}
    chat_users_list = []
    chat_users_post_list = []
    receive_user = MyUser.objects.filter(pk=pk)
    for list in receive_user:
        chat_users = ChatModel.objects.filter(send_user=request.user, receive_user=list)
        chat_switch_users = ChatModel.objects.filter(send_user=list, receive_user=request.user)
    for i in range(len(chat_users)):
        chat_users_list.append(chat_users[i].pk)
    for j in range(len(chat_switch_users)):
        chat_users_list.append(chat_switch_users[j].pk)
    chat_users_list.sort()
    for i in range(len(chat_users_list)):
        chat_users_post_list.append(ChatModel.objects.filter(pk=chat_users_list[i]))
    context['chat_form'] = ChatForm
    context['chat_pk'] = pk
    context['chat_users'] = chat_users_post_list
    return render(request, 'chat.html', context)

