from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User


class UserLoginForm(AuthenticationForm):

    """Если нижний способ в верстке """
    username = forms.CharField()
    password = forms.CharField()

    """Если верхний способ в верстке """
    # username = forms.CharField(
    #     label='Имя',
    #     widget=forms.TextInput(attrs={
    #         "autofocus": True,
    #         'class': 'form-control',
    #         'placeholder': "Введите ваше имя пользователя",
    #     }
    #     )
    # )
    # password = forms.CharField(
    #     label='Пароль',
    #     widget=forms.PasswordInput(attrs={
    #         "autocomplete": "current-password",
    #         'class': 'form-control',
    #         'placeholder': "Введите ваш пароль",
    #     }
    #     ),
    # )

    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password_1",
            "password_2",
        )

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password_1 = forms.CharField()
    password_2 = forms.CharField()
