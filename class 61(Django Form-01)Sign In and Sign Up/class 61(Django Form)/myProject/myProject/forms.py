from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from myApp.models import *
from django import forms

class myUsercreationForm(UserCreationForm):
    class Meta:
        model = customuser
        fields=UserCreationForm.Meta.fields+("city","profile_pic","usertype")


class myauthenticationform(AuthenticationForm):
    class Meta:
        model = customuser
        fields=("username","password")