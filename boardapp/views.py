from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from accountapp.models import MyUser
from boardapp.models import Board_Model, Board_Gonge_Model, Board_Jaro_Model


def board_list(request):
    context={}

    page = request.GET.get('page', '1')

    board = Board_Model.objects.all().order_by('-board_date_time')
    count = len(board)

    paginator = Paginator(board, 8)

    page_obj = paginator.get_page(page)

    context['board'] = page_obj
    context['count'] = count

    return render(request, 'board_list.html', context)

def board_write(request, pk):
    context={}

    if request.method == 'POST' and request.POST.get('board_submit1'):
        print(request.POST)
        print('33333333333333333')
        print(request.FILES)

        user = MyUser.objects.filter(pk=pk)

        for temp_user in user:
            board = Board_Model(board_user=temp_user, board_title=request.POST.get('title'), board_detail=request.POST.get('context'), board_file=request.FILES.get('file'))
            board.save()

    context['pk'] = pk
    return render(request, 'board_write.html', context)

def board_detail(request, title):
    context={}

    board = Board_Model.objects.filter(pk=title)
    data = ''
    for temp in board:
        context['user'] = temp.board_user
        context['title'] = temp.board_title
        for temp_data in temp.board_detail:
            if temp_data == ' ':
                data += '∠'
            elif temp_data == '\r':
                data += '∏'
            else:
                data += temp_data
        context['detail'] = data
        print(data)
        context['file'] = temp.board_file

    return render(request, 'board_detail.html', context)

def board_gonge_list(request):
    context={}

    page = request.GET.get('page', '1')

    gonge = Board_Gonge_Model.objects.all().order_by('-board_gonge_date_time')
    count = len(gonge)

    paginator = Paginator(gonge, 8)

    page_obj = paginator.get_page(page)

    context['gonge'] = page_obj
    context['count'] = count

    return render(request, 'board_gonge_list.html', context)

def board_gonge_detail(request, title):
    context={}

    gonge = Board_Gonge_Model.objects.filter(pk=title)
    data = ''
    for temp in gonge:
        context['user'] = temp.board_gonge_user
        context['title'] = temp.board_gonge_title
        for temp_data in temp.board_gonge_detail:
            if temp_data == ' ':
                data += '∠'
            elif temp_data == '\r':
                data += '∏'
            else:
                data += temp_data
        context['detail'] = data
        print(data)
        context['file'] = temp.board_gonge_file

    return render(request, 'board_gonge_detail.html', context)

def board_jaro_list(request):
    context={}

    page = request.GET.get('page', '1')

    jaro = Board_Jaro_Model.objects.all().order_by('-board_jaro_date_time')
    count = len(jaro)

    paginator = Paginator(jaro, 8)

    page_obj = paginator.get_page(page)

    context['jaro'] = page_obj
    context['count'] = count

    return render(request, 'board_jaro_list.html', context)

def board_jaro_detail(request, title):
    context={}

    jaro = Board_Jaro_Model.objects.filter(pk=title)
    data = ''
    for temp in jaro:
        context['user'] = temp.board_jaro_user
        context['title'] = temp.board_jaro_title
        for temp_data in temp.board_jaro_detail:
            if temp_data == ' ':
                data += '∠'
            elif temp_data == '\r':
                data += '∏'
            else:
                data += temp_data
        context['detail'] = data
        print(data)
        context['file'] = temp.board_jaro_file

    return render(request, 'board_jaro_detail.html', context)