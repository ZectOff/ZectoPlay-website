from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *
from django.db import models
from .forms import UserRegisterForm,UserLoginForm,UserProfileForm
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
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
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username,password=password)
            login(request,user)
            return redirect('user_profile')
        else:
            messages.error(request, 'Ошибка авторизации') # Не выводиться
    else:
        form = UserLoginForm()
    return render(request, 'headset/login.html', {"form": form})

def user_logout(request):
    auth.logout(request)
    messages.info(request,'You loggen out')
    return redirect('/')
def user_profile(request):
    context = {'user':request.user}
    return render(request,'headset/user_profile.html',context)