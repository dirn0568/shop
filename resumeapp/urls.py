from django.contrib import admin
from django.urls import path, include

from resumeapp import views

app_name = 'resumeapp'

urlpatterns = [
    path('create_resume/<int:pk>/', views.create_resume, name='create_resume'),
    path('update_resume/<int:pk>/', views.update_resume, name='update_resume'),
    path('delete_resume/<int:pk>/', views.delete_resume, name='delete_resume'),
    path('list_resume/<int:pk>/', views.list_resume, name='list_resume'),
    path('detail_resume/<int:pk1>/<int:pk2>', views.detail_resume, name='detail_resume'),

    path('test_resume/<int:test1>/<int:test2>/<int:test3>/<int:pk>/', views.test_resume, name='test_resume'),

    path('test_resume2/<int:school>/<int:pk>/', views.test_resume2, name='test_resume2'),

    path('test_calender', views.test_calender, name='test_calender'),

    path('test_test', views.test_test, name='test_test'),

    path('button_test', views.button_test, name='button_test'),
]