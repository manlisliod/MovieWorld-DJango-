from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import CreateView
from django.contrib.auth import get_user_model


def LoginView(request):
    if request.method == "POST":     
        username = request.POST.get('username')
        password = request.POST.get('password') 
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('post-list')
    return redirect('post-list')


def RegisterView(request):
    if request.method=="POST":
        r = request.POST
        username = r.get('username')
        email = r.get('email')
        first_name=r.get('firstName')
        last_name = r.get('lastName')
        password = r.get('password')
        repeatPassword = r.get('repeatPassword')
        if password!=repeatPassword:
            raise ValidationError('Passwords do not match')
        user= get_user_model().objects.create(username=username,email=email,first_name=first_name,last_name=last_name)
        user.set_password('password')
        user.save()
        login(request,user)
        return redirect('post-list')
    else:
        return redirect('post-list')

