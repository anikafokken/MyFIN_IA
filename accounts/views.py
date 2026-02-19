from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
import forms

# Create your views here.


class SignUpView(CreateView):
    form_class = forms.SignUpForm
    success_url = reverse_lazy("login") # redirect users after registration to login
    template_name = "registration/signup.html"
    
    
        
