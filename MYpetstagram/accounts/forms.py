from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms
from MYpetstagram.accounts.models import PetstagramUser


class PetstagramUserCreateForm(UserCreationForm):
    class Meta:
        model = PetstagramUser
        fields = (
            'username',
            'email',
        )


class PetstagramUserEdirForm(forms.ModelForm):
    class Meta:
        model = PetstagramUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'profile_picture',
            'gender',
        )
        exclude = ('password',)
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'profile_picture': 'Image',
            'gender': 'Gender',
        }


class UserLoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'placeholder': 'Username',
            }
        )
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autofocus': True,
                'placeholder': 'Password',
            }
        )
    )

