from django.contrib import admin

from messageapp.models import Message_Resume_Model, Test_Data, Message_Receive_Model

admin.site.register(Message_Receive_Model)

admin.site.register(Message_Resume_Model)
admin.site.register(Test_Data)