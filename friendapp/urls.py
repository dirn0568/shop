
from django.contrib import admin
from django.urls import path, include

from friendapp import views

app_name = 'friendapp'

urlpatterns = [
    path('create_friend/<word1>/<word2>', views.createfriendview, name='create_friend'),
    path('friend_list/<int:pk>', views.detailfriendview, name='friend_list'),
    path('delete_friend/<user>/<user_friend>/', views.deletefriendview, name='delete_friend'),
]