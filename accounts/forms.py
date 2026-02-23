from django import forms
from django.db import models
from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = CustomUser.REQUIRED_FIELDS
        widgets = { # create forms dependent on user account type
            'first_name': forms.TextInput(attrs={'class': 'dependent-field student-only'}),
            'last_name': forms.TextInput(attrs={'class': 'dependent-field student-only'}),
            'school_name': forms.TextInput(attrs={'class': 'dependent-field school-only'}),
            'admin_code': forms.TextInput(attrs={'class': 'dependent-field admin-only'}),
        }

print(SignUpForm.as_p) # render as elements
