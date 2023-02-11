from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm

UserModel = get_user_model()


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'password1', 'password2')
        field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].help_text = None


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
            }
        )
    )

    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password'
            }
        )
    )

# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = UserModel
#         fields = ('username', 'password')
#         widgets = {
#             'username': forms.TextInput(attrs={
#                 'placeholder': 'Username'
#             })
#         }

# def __init__(self, *args, **kwargs):
#     self.request = kwargs.pop('request', None)
#     super(LoginForm, self).__init__(*args, **kwargs)
