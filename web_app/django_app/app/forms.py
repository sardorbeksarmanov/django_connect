from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=60)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()


class LoginForm(forms.Form):
    username_or_email = forms.CharField(max_length=120)
    password = forms.CharField(widget=forms.PasswordInput)
