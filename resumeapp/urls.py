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

    path('resume_1/<int:school>/<int:school_major4>/<int:career>/<int:pk>/', views.resume_1, name='resume_1'),

    path('test_test', views.test_test, name='test_test'),

    path('test_test2', views.test_test2, name='test_test2'),

    path('test_test3', views.test_test3, name='test_test3'),

    path('resume_resume1/<int:pk>', views.resume_resume1, name='resume_resume1'),

    path('resume_resume2/<int:school>/<int:school_major4>/<int:career>/<int:out_play>/<int:prize_play>/<int:port_polio>/<int:self_introduce>/<int:pk>', views.resume_resume2, name='resume_resume2'),

    path('resume_resume3/<int:title>/<int:pk>', views.resume_resume3, name='resume_resume3'),

    path('resume_resume4/<int:title>/<int:career>/<int:company_ability>/<int:company_project>/<int:pk>', views.resume_resume4, name='resume_resume4'),

    path('resume_resume5/<int:title>/<int:pk>', views.resume_resume5, name='resume_resume5'),

    path('trash_test', views.trash_test, name='trash_test'),

    path('trash_test2', views.trash_test2, name='trash_test2'),

    path('resume_write/<int:school>/<int:school_major4>/<int:career>/<int:out_play>/<int:prize_play>/<int:port_polio>/<int:self_introduce>/<int:company_ability>/<int:company_project>/<int:pk>', views.resume_write, name='resume_write'),
]