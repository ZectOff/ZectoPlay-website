from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *
from django.db import models
from .forms import UserRegisterForm,UserLoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request,'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'headset/registration.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main_page')
        else:
            messages.error(request, 'Ошибка авторизации') # Не выводиться
    else:
        form = UserLoginForm()
    return render(request, 'headset/login.html', {"form": form})
