from django.forms import ModelForm
from django import forms
from .models import ToDo


class CrateForm(ModelForm):

    class Meta:
        model = ToDo
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)