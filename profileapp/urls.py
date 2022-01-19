from django.contrib import admin
from django.urls import path, include

from profileapp import views

app_name = 'profileapp'

urlpatterns = [
    path('create_profile/<int:pk>/', views.create_profile, name='create_profile'),
    path('update_profile/<int:pk>/', views.update_profile, name='update_profile'),
    path('delete_profile/<int:pk>/', views.delete_profile, name='delete_profile'),

    path('detail_user_update/<int:pk>/', views.detail_user_update, name='detail_user_update'),
]