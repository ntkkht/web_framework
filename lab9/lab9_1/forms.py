from django import forms
from django.core.exceptions import ValidationError
from lab9_1.models import Member
from django.forms import  TextInput
from django.utils.translation import gettext_lazy as _

class LoginForm(forms.Form):
    username = forms.CharField(max_length=13, widget=TextInput(), label="username" ,required=True)
    password = forms.CharField(max_length=256, widget=TextInput(), label="password", required=True)