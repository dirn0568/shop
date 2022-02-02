from django.shortcuts import render

# Create your views here.

def board_list(request):
    context={}

    return render(request, 'board_list.html', context)