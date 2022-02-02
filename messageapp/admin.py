from django.contrib import admin

from messageapp.models import Message_Resume_Model, Message_Send_Model, Test_Data

admin.site.register(Message_Send_Model)

admin.site.register(Message_Resume_Model)
admin.site.register(Test_Data)