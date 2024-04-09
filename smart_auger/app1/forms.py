from django import forms
from .models import data_management_model

class data_management_form(forms.ModelForm):
    class Meta:
        model = data_management_model
        exclude = ['timestamp']

class user_management_form(forms.ModelForm):
    class Meta:
        model = data_management_model
        fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)