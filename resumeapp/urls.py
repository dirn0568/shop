from django.contrib import admin
from django.urls import path, include

from resumeapp import views

app_name = 'resumeapp'

urlpatterns = [
    path('create_resume/<int:pk>/', views.create_resume, name='create_resume'),
    path('update_resume/<int:pk>/', views.update_resume, name='update_resume'),
    path('delete_resume/<int:pk>/', views.delete_resume, name='delete_resume'),
    path('list_resume/<int:pk>/', views.list_resume, name='list_resume'),
    path('detail_resume/<int:title>/<int:pk>', views.detail_resume, name='detail_resume'),

    path('resume_resume2/<int:school>/<int:school_major4>/<int:career>/<int:out_play>/<int:prize_play>/<int:port_polio>/<int:self_introduce>/<int:pk>', views.resume_resume2, name='resume_resume2'),

    path('resume_resume3/<int:title>/<int:pk>', views.resume_resume3, name='resume_resume3'),

    path('resume_resume4/<int:title>/<int:career>/<int:company_ability>/<int:company_project>/<int:pk>', views.resume_resume4, name='resume_resume4'),

    path('resume_resume5/<int:title>/<int:pk>', views.resume_resume5, name='resume_resume5'),

    #############################################################################################################################################
    path('resume_resume2_update/')
    #############################################################################################################################################

    path('resume_write/<int:school>/<int:school_major4>/<int:career>/<int:out_play>/<int:prize_play>/<int:port_polio>/<int:self_introduce>/<int:company_ability>/<int:company_project>/<int:pk>', views.resume_write, name='resume_write'),
]