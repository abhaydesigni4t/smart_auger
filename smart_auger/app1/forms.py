from django import forms
from .models import data_management_model,user_management_model,Location

class data_management_form(forms.ModelForm):
    class Meta:
        model = data_management_model
        exclude = ['timestamp']

class user_management_form1(forms.ModelForm):
    class Meta:
        model = user_management_model
        fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['rec_no', 'latitude', 'longitude']
