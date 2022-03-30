from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from accountapp import views
from accountapp.views import Create_User, Detail_User, Update_User, Delete_User, Create_Company_User

app_name = 'accountapp'

urlpatterns = [
    path('create_user/', Create_User.as_view(), name='create_user'),
    path('create_company_user/', Create_Company_User.as_view(), name='create_company_user'),
    path('detail_user/<int:pk>/', Detail_User.as_view(), name='detail_user'),
    path('update_user/<int:pk>/', Update_User.as_view(), name='update_user'),
    path('delete_user/<int:pk>/', Delete_User.as_view(), name='delete_user'),

    path('popup/', views.popup, name='popup'),

    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    # path('company_login/',  views.company_login_view, name='company_login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create_friend/<friend1>/<friend2>/<int:pk>/', views.createfriend, name='createfriend'),
]