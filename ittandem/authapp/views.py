from django.shortcuts import render, reverse
from django.views.generic.detail import DetailView
from .models import User



class UserProfile(DetailView):
    model = User
    template_name = 'authapp/profile.html'


def login(request):
    return render(request, 'authapp/login.html')


def register(request):
    return render(request, 'authapp/register.html')


def profile(request):
    return render(request, 'authapp/profile.html')
