from django.contrib import admin
from django.urls import path, include

from chatapp import views

app_name = 'chatapp'

urlpatterns = [
    path('talk/<int:pk>', views.chatview, name='chat'),
]