from django import forms
from django.forms import ModelForm
from ex.models import Tip

class SignUpForm(forms.Form):
    username = forms.CharField(label='Enter your name', max_length=128)
    password = forms.CharField(label='Enter your password', widget=forms.PasswordInput())
    password_verification = forms.CharField(label='Password validation', widget=forms.PasswordInput())


class SignInForm(forms.Form):
    username = forms.CharField(label='Enter your name', max_length=128)
    password = forms.CharField(label='Enter your password', widget=forms.PasswordInput())


class TipForm(ModelForm):
    class Meta:
        model = Tip
        fields = ['content']

