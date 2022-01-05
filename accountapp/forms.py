from django import forms
from django.contrib.auth.forms import UserCreationForm

from accountapp.models import MyUser



class Create_User_Form(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = UserCreationForm.Meta.fields + ('nickname',)


class Update_User_Form(Create_User_Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True

class Create_Company_User_Form(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = UserCreationForm.Meta.fields + ('nickname',)