from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.forms import ModelForm, TextInput, Textarea


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='',
                               widget=forms.PasswordInput(attrs = {'class': 'registration__input',
                                                                   'placeholder': 'Введите пароль'}), )
    password2 = forms.CharField(label='',
                                widget=forms.PasswordInput(attrs = {'class': 'registration__input',
                                                                    'placeholder': 'Повторите пароль'}), )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        labels = {
            'username': '', 'first_name': '', 'email': ''
        }
        help_texts = {
            'username': ' ',
        }
        widgets = {
            'username': TextInput(attrs={
                'class': 'registration__input', 'placeholder': 'Имя пользователя'
            }),
            'first_name': TextInput(attrs={
                'class': 'registration__input', 'placeholder': 'Имя'
            }),
            'email': TextInput(attrs={
                'class': 'registration__input', 'placeholder': 'Адрес электронной почты'
            }),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        labels = {
            'first_name': '', 'last_name': '', 'email': ''
        }
        widgets = {
            'first_name': TextInput(attrs={
                'class': 'registration__input', 'placeholder': 'Имя пользователя'
            }),
            'last_name': TextInput(attrs={
                'class': 'registration__input', 'placeholder': 'Имя'
            }),
            'email': TextInput(attrs={
                'class': 'registration__input', 'placeholder': 'Адрес электронной почты'
            }),
        }
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
        labels = {
            'date_of_birth': '', 'photo': ''
        }
        help_texts = {
            'date_of_birth': ' ',
        }
        widgets = {
            'date_of_birth': TextInput(attrs={
                'class': 'registration__input', 'placeholder': 'Дата рождения'
            })}

class Login(forms.Form):
    login = forms.CharField(label='Логин', max_length=25),
    password = forms.CharField(label='Пароль', max_length=25, widget=forms.PasswordInput),

