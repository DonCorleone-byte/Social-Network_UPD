from django import forms
from .models import Comment
from django.forms import ModelForm, TextInput, Textarea

class EmailPostForm(forms.Form):
   # name = forms.CharField(max_length=25)
    name = forms.CharField(label='', max_length=25,
                               widget=forms.TextInput(attrs={'class': 'repost__form-input',
                                                                 'placeholder': 'Введите имя'}), )


    email = forms.EmailField(label='',
                       widget=forms.TextInput(attrs={'class': 'repost__form-input',
                                                     'placeholder': 'Введите ваш email'}), )
    #email = forms.EmailField()
    to = forms.EmailField(label='',
                       widget=forms.TextInput(attrs={'class': 'repost__form-input',
                                                     'placeholder': 'Введите email получателя'}), )
    comments = forms.CharField(label='' ,required=False,
                               widget=forms.Textarea(attrs={'class': 'repost__form-textarea',
                                                            'placeholder': 'Введите комментарий'}),)

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

