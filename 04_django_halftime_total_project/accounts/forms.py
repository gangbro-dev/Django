from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

class UserForm():
    pass


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = (
            'email',
            'first_name',
            'last_name',
        )