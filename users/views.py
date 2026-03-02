import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from accounts import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


# Create your views here.

def register(request):
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('portal_view')
    else:
        form = forms.SignUpForm()
    return render(request, 'templates/registration/signup.html')