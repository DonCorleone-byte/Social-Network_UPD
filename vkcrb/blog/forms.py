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
        fields = ('name', 'body')
        labels = {
            'name': '', 'body': ''

        }
        widgets = {
            'name': TextInput(attrs={
                'class': 'comments__form-input','placeholder':'Введите имя'
            }),

            'body': TextInput(attrs={
                'class': 'comments__form-input', 'placeholder': 'Введите комментарий'
            })
        }

