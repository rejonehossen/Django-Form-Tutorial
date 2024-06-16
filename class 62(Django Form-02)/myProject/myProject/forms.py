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
    
    
    
    
class addcategotyform(forms.ModelForm):
    class Meta:
        model = categorymodel
        # fields= "__all__"
        exclude=["update_at","create_at","created_by"]
        

class addtaskform(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields= ["priotiry","taskname","description","status","due_date","date","completed_date"]
        
        widgets={
            'due_date':forms.DateInput(attrs={'type':'date',}),
            'date':forms.DateInput(attrs={'type':'date',}),
            'completed_date':forms.DateInput(attrs={'type':'date',}),
            
        }
        
        labels={
            'priotiry': "Select Priority",
            'taskname':'Enter Task Name',
        }