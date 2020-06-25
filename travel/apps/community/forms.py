from django import forms
from django_registration.forms import RegistrationForm as BaseRegistrationForm
from apps.accounts.models import CustomerUser
from apps.utils.forms import BaseBootstrapForm, FieldKwargsMeta
from django.utils.translation import gettext as _


# For the class based is for user login
class CommunitySignUpForm(FieldKwargsMeta, BaseBootstrapForm, BaseRegistrationForm):
    referal = forms.CharField(
            required=True,
            label=_("Referred by"),
            help_text=_("Enter the referal code ."),
    )

    password1 = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control first',
        }),
        help_text=_('Use at least 8 characters. Do not use a password from another site or a term that is too '
                    'obvious, such as your pet’s name'),
    )

    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control last',
        }),
        help_text=_("Enter the same password as above, for verification."),
    )

    class Meta(BaseRegistrationForm.Meta):
        # Preparing vars to add the new user
        BASE_REGISTRATION_FIELDS = BaseRegistrationForm.Meta.fields
        model = CustomerUser
        fields = [
                 ] + BASE_REGISTRATION_FIELDS

    def clean_referal(self) -> str:
        code = self.cleaned_data.get('referal')
        if code:
            if not CustomerUser.objects.filter(ref_code=code).exists():
                raise forms.ValidationError(_('Invalid referal code'), code='invalid_code')
        return code


# this class is for login
class SignInForm(forms.Form):
    """
    The Login form where we make able our user to login on the dashboard.

    Args:
        email: The user's email(username).
        password: the password field.

    Returns: The cleaned form to proceed to the according View.
    """
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': _('Email'),
                'class': 'form-control',
            },
        ),
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': _('Password'),
                'class': 'form-control',
            },
        ),
    )


class CompleteProfileForm(BaseBootstrapForm, forms.ModelForm):
    class Meta:
        model = CustomerUser
        fields = (
            'avatar',
            'first_name',
            'last_name',
        )
