from django import forms
from django.contrib.auth.models import User
from .models import Message


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', )

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class SearchForm(forms.Form):
    class Meta:
        model = Message
        fields = ('text', )

class AddContactForm(forms.Form):
    contact_id = forms.HiddenInput()

class MessageForm(forms.Form):
    text = forms.CharField(max_length=500)
