from django.contrib import admin
from django.urls import path, include

from mainapp import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('main2', views.main2, name='main2'),

    path('company_popup/<int:company_number>', views.company_popup, name='company_popup'),

    path('search_report/', views.SearchReportView.as_view(), name='search_report'),
]