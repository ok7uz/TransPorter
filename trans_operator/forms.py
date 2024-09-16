from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class OperatorCreateForm(forms.Form):
    name = forms.CharField(max_length=100, label='Имя', widget=forms.TextInput(attrs={'class': 'border-dark'}))
    username = forms.CharField(max_length=100, label='Логин', widget=forms.TextInput(attrs={'class': 'border-dark'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'border-dark'}), label='Пароль')

    def save(self):
        cleaned_data = self.cleaned_data
        user = User(first_name=cleaned_data['name'], username=cleaned_data['username'])
        user.set_password(cleaned_data['password'])
        user.save()
        return user

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Пользователь с таким именем уже существует.')
        if validate_password(password) is not None:
            raise ValidationError(validate_password(password))
        return cleaned_data
