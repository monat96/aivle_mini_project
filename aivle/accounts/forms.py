from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth import get_user_model


class CustomUserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = CustomUser
        fields = ("username", "email", "nickname")


class UserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].disabled = True

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'nickname')