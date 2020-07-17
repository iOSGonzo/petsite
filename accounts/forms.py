from django.contrib.auth.models import User
from django import forms

class SignupView(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'password']
