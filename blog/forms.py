from django import forms

from .models import Post
# import the built in form AND model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'content']


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        # fields come from built in user model. Read documentaion to see all available fields
        fields = ['username', 'email', 'password1', 'password2']
