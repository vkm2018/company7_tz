from django.contrib.auth.forms import AuthenticationForm

from apps.account.models import User


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ('username', 'password')
