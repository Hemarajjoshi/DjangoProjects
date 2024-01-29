from django import forms
from . models import Viewers, Paticipant 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta : 
        model = Viewers
        fields = '__all__'
    


class ViewerRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class ParticipantRegistartionForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Paticipant
        fields = '__all__'


