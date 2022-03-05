from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError


class RegistrationForm(forms.ModelForm):
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput) # widget kropkuje hasło, bez () bo klasa

    class Meta:
        model = get_user_model()
        fields = ('email', 'fullname', 'is_instructor', 'password')

    def clean_password2(self):  # customowa validacja hasła
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise ValidationError('Password dont match')
        return password2

    def save(self, commit=True):
        user = super().save(commit=True)

        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = ('username', 'password')
