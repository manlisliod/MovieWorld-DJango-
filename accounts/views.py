from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.contrib import messages


def LoginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'You have successfully login')
            return redirect('post-list')
        messages.error(request, 'Wrong credentials')
    return redirect('post-list')


def RegisterView(request):
    if request.method == "POST":
        r = request.POST
        username = r.get('username')
        email = r.get('email')
        first_name = r.get('firstName')
        last_name = r.get('lastName')
        password = r.get('password')
        repeatPassword = r.get('repeatPassword')
        if password != repeatPassword:
            raise ValidationError('Passwords do not match')
        # check if already a user exists in the database
        user = get_user_model().objects.filter(username=username)
        if user.exists() and user.count() < 2:
            messages.error(request, 'Username already exists')
            return redirect('post-list')
        user = get_user_model().objects.create(username=username, email=email,
                                               first_name=first_name, last_name=last_name)
        user.set_password('password')
        user.save()
        login(request, user)
        messages.success(
            request, 'Account successfully created you are now logged in')
        return redirect('post-list')
    else:
        return redirect('post-list')
