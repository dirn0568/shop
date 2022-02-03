from django.contrib import admin
from django.urls import path, include

from boardapp import views

app_name = 'boardapp'

urlpatterns = [
    path('board_list', views.board_list, name='board_list'),
    path('board_write/<int:pk>', views.board_write, name='board_write'),
    path('board_detail/<int:title>', views.board_detail, name='board_detail'),

    path('board_gonge_list', views.board_gonge_list, name='board_gonge_list'),
    path('board_gonge_detail/<int:title>', views.board_gonge_detail, name='board_gonge_detail'),

    path('board_jaro_list', views.board_jaro_list, name='board_jaro_list'),
    path('board_jaro_detail/<int:title>', views.board_jaro_detail, name='board_jaro_detail'),
]