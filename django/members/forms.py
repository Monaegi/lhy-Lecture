from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        self.base_fields['username'].widget.attrs['class'] = 'form-control'
        self.base_fields['username'].widget.attrs['placeholder'] = 'Username'
        self.base_fields['password'].widget.attrs['class'] = 'form-control'
        self.base_fields['password'].widget.attrs['placeholder'] = 'Password'
        super().__init__(*args, **kwargs)