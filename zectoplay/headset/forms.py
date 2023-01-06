from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label = 'Имя пользователя',help_text = 'Имя пользователя состоит максимум из 150 символов',widget=forms.TextInput(attrs={'class':'form-control','autocomplete':'off'}))
    password1 = forms.CharField(label= 'Пароль',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    model = User
    fields = ('username','password1','password2')

class UserLoginForm(AuthenticationForm):
    username =  forms.CharField(label = 'Имя пользователя',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label = 'Пароль',widget=forms.PasswordInput(attrs={'class':'form-control'}))