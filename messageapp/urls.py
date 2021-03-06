from django.urls import path, include

from messageapp import views

app_name = 'messageapp'

urlpatterns = [
    path('message_box/<int:pk>', views.friend_request_message, name='message_box'),
    path('delete_message/<int:pk>', views.delete_message, name='delete_message'),

    path('message_content/<int:pk>', views.message_content, name='message_content'),
    path('message_send/<int:pk>', views.message_send, name='message_send'),
    path('message_write/<int:pk>', views.message_write, name='message_write'),
    path('message_search/<int:pk>', views.message_search, name='message_search'),
    path('message_propose/<int:pk>', views.message_propose, name='message_propose'),

    path('message_content_detail/<int:title>/<int:pk>', views.message_content_detail, name='message_content_detail'),
    path('message_send_detail/<int:title>/<int:pk>', views.message_send_detail, name='message_send_detail'),
    path('message_propose_detail/<int:title>/<int:pk>', views.message_propose_detail, name='message_propose_detail'),

    path('message_test', views.test, name='test'),
]