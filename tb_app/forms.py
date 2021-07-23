from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'type': 'email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password', 'type': 'password'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password Confirmation', 'type': 'password'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password', 'type': 'password'}))

    class Meta:
        model = User
        fields = ['username', 'password']
