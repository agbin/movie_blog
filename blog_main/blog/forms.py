from django import forms
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    # background = forms.FileField()
    # movie_image = forms.FileField()
    # movie_image_b = forms.FileField()
    class Meta:
        model = Post
        fields = ('quota', 'title', 'text', 'background', 'movie_image', 'movie_image_b')


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class CommentAddForm(forms.ModelForm):
    text = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'form-control',
               'placeholder': 'Jeżeli oglądałeś ten film albo masz na jego temat jakieś przemyślenia, '
                              'to pisz..', }
    ))
    name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Imię:', 'size': '15px'}))

    class Meta:
        model = Comment
        fields = ('name', 'text')


class SearchForm(forms.Form):
    q = forms.CharField(max_length=64)


