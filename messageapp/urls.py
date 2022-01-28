from django.urls import path, include

from messageapp import views

app_name = 'messageapp'

urlpatterns = [
    path('message_box/<int:pk>', views.friend_request_message, name='message_box'),
    path('delete_message/<int:pk>', views.delete_message, name='delete_message'),

    path('message_content/<int:pk>', views.message_content, name='message_content'),
]