from django.contrib import admin

# Register your models here.
from boardapp.models import Board_Model, Board_Gonge_Model, Board_Jaro_Model

admin.site.register(Board_Model)
admin.site.register(Board_Gonge_Model)
admin.site.register(Board_Jaro_Model)
