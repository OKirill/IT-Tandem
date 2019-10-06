from django.shortcuts import render, reverse
from django.views.generic.detail import DetailView
from .models import User



class UserProfile(DetailView):
    model = User
    template_name = 'authapp/profile.html'