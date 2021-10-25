from django.forms import ModelForm

from profileapp.models import User_Profile


class ProfileForm(ModelForm):
    class Meta:
        model = User_Profile
        fields = ['profile_text', 'profile_img']

class Update_ProfileForm(ProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)