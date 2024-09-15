from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise ValidationError('Неверное имя пользователя или пароль.')

        return cleaned_data
