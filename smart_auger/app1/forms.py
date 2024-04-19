from django import forms
from .models import user_management_model,Location


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
        fields = ['latitude', 'longitude']

