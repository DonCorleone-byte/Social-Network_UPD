from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.forms import ModelForm, TextInput, Textarea


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Введите имя'
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Введите email'
            }),
            'email': TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Введите комментарий'
            })
        }
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
        widgets = {
            'date_of_birth': TextInput(attrs={
                'class': 'date'
            })}

class Login(forms.Form):
    login = forms.CharField(label='Логин', max_length=25),
    password = forms.CharField(label='Пароль', max_length=25, widget=forms.PasswordInput),
