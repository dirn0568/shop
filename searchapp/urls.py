from django.contrib import admin
from django.urls import path, include

from searchapp import views

app_name = 'searchapp'

urlpatterns = [
    path('search_resume', views.search_resume, name='search_resume'),
]