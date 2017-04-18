from django.contrib.auth.forms import UserCreationForm
from .models import User, Comment
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'address', 'email')

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)
