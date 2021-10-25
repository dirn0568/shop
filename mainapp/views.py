from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from accountapp.models import MyUser


def main(request):
    test_user = MyUser.objects.filter()
    context = {}
    context['test_user'] = test_user
    return render(request, 'main.html', context)