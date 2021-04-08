from django import forms
from .models import Comment
from django.forms import ModelForm, TextInput, Textarea

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control','placeholder':'Введите имя'
            }),
            'email': TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Введите email'
            }),
            'body': Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Введите комментарий'
            })
        }

