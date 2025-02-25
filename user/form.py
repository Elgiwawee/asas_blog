from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import activate, gettext_lazy as _
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        # Activate the desired language when the form is initialized
        activate('ar')  # Replace 'ar' with the desired language code
        super().__init__(*args, **kwargs)


    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': _('Username'),
            'email': _('Email'),
            'password1': _('Password'),
            'password2': _('Confirm Password'),
        }