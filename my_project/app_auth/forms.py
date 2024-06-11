from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import CharField, TextInput, PasswordInput


class UploadAuthorsForm(forms.Form):
    authors_file = forms.FileField()

class UploadQuotesForm(forms.Form):
    quotes_file = forms.FileField()


class RegisterForm(UserCreationForm):
    username = CharField(max_length=16, min_length=3, required=True, widget=TextInput(attrs={'class': 'form-control'}))
    email = CharField(max_length=25, required=True, widget=TextInput(attrs={'class': 'form-control'}))
    password1 = CharField(required=True, widget=PasswordInput(attrs={'class': 'form-control'}))
    password2 = CharField(required=True, widget=PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = CharField(max_length=16, min_length=3, required=True, widget=TextInput(attrs={'class': 'form-control'}))
    password = CharField(required=True, widget=PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password')

