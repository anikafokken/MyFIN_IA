from django import forms
from django.db import models
from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        username = forms.CharField(max_length=100, required=False)
        school_name = forms.CharField(max_length=100, required=False)
        fields = ['username', 'password1', 'password2', 'account_type', 'first_name', 'last_name', 'school_name', 'email']
        widgets = { # create forms dependent on user account type
            'first_name': forms.TextInput(attrs={'class': 'dependent-field student-only'}),
            'last_name': forms.TextInput(attrs={'class': 'dependent-field student-only'}),
            'school_name': forms.TextInput(attrs={'class': 'dependent-field school-only'}),
            # 'admin_code': forms.TextInput(attrs={'class': 'dependent-field admin-only'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        account_type = cleaned_data.get("account_type")

        if account_type == "STUDENT":
            if not cleaned_data.get("first_name"):
                self.add_error('first_name', "First name is required.")
            if not cleaned_data.get("last_name"):
                self.add_error('last_name', "Last name is required.")
            if not cleaned_data.get("username"):
                self.add_error('username', "Username is required.")
        if account_type == "SCHOOL":
            if not cleaned_data.get("school_name"):
                self.add_error('school_name', "School name is required for school accounts.")
        # if account_type == "ADMIN":
        #     if not cleaned_data.get("admin_code"):
        #         self.add_error('admin_code', "Please enter a valid admin authorization code.")
        return cleaned_data

print(SignUpForm.as_p) # render as elements
