from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'user-input-bar','autocomplete':'off', 'size':46, 'type':'text', 'required': None, 'placeholder':'Введите имя'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class':'user-input-bar','autocomplete':'off', 'size':46, 'type':'password', 'required': True, 'placeholder':'Введите пароль'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class':'user-input-bar','autocomplete':'off', 'size':46, 'type':'password', 'required': True, 'placeholder':'Повторите пароль'}))
    model = User
    fields = ('username','password1','password2')

class UserLoginForm(AuthenticationForm):
    username =  forms.CharField(widget=forms.TextInput(attrs={'class':'user-input-bar','autocomplete':'off', 'size':46, 'type':'text', 'placeholder':'Введите имя'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class':'user-input-bar','autocomplete':'off', 'size':46, 'type':'password', 'placeholder':'Введите пароль'}))