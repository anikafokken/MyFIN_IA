from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts import forms
from django.contrib.auth import views as views_auth
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


# Create your views here.

class SignUpView(CreateView):
    form_class = forms.SignUpForm
    success_url = reverse_lazy('portal_view') # redirect users after registration to login
    template_name = "registration/signup.html"


class LoginViews(views_auth.LoginView):
    # redirect_authenticated_user = True

    def get_success_url(self):
        print(type(self.request.user))
        if self.request.user.is_active:
            return reverse('portal_view')
        return '/'



    
    
        
