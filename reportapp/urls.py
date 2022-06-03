from django.contrib import admin
from django.urls import path, include

from reportapp import views

app_name = 'reportapp'

urlpatterns = [
    path('report_user/<int:user1>/<int:user2>', views.report_user, name='report_user'),
]