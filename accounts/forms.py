from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Create your tests here.


class AddUserForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'field', 'placeholder': 'PASSWORD'}), label="")
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'field', 'placeholder': 'REPEAT PASSWORD'}), label="")

    class Meta:
        model = User
        fields = ['username']

        help_texts = {
            'username': ''
        }

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'USERNAME', 'class': 'field'}),
        }

        labels = {
            'username': ""
        }

    def clean(self):
        data = super().clean()
        if data['password1'] != data['password2']:
            raise ValidationError('Hasła się nie zgadzają!')
        return data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=128, widget=forms.TextInput(
        attrs={'class': 'field', 'placeholder': 'LOGIN'}), label="")
    password = forms.CharField(max_length=128, widget=forms.PasswordInput(
        attrs={'class': 'field', 'placeholder': 'HASŁO'}), label="")
