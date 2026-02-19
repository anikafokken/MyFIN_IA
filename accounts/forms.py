from django import forms
from django.db import models

class SignUpForm(forms.ModelForm):
    class Meta:
        username = models.CharField(max_length=20)
        password = models.CharField(max_length=40)
        email = models.EmailField()
        CHOICES = (('Student', 'School', 'Admin'))
        account_type = forms.ChoiceField(choices=CHOICES)

print(SignUpForm.as_p()) # render as elements
