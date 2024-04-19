from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "password1",
            "password2",
            'age',
            'gender',
        ]

class CustomProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = [
            'profile_image',
        ]