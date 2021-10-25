from django.contrib import admin

# Register your models here.
from accountapp.models import MyUser, Friend_List

admin.site.register(MyUser)
admin.site.register(Friend_List)