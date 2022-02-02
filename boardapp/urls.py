from django.contrib import admin
from django.urls import path, include

from boardapp import views

app_name = 'boardapp'

urlpatterns = [
    path('board_list', views.board_list, name='board_list'),
]