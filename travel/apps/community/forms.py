from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django_registration.forms import RegistrationForm as BaseRegistrationForm
from apps.accounts.models import CustomerUser
from apps.utils.forms import BaseBootstrapForm, FieldKwargsMeta

from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordResetForm,
    SetPasswordForm,
    PasswordChangeForm,
)
from django.utils.translation import gettext as _



class CommunitySignUpForm(FieldKwargsMeta, BaseBootstrapForm, BaseRegistrationForm):
    password1 = forms.CharField(label=_("Password"),
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control first',
                                }),
                                help_text=_('Use at least 8 characters. Do not use a password from another site or a term that is too obvious, such as your pet\'s name.'))
    password2 = forms.CharField(label=_("Password confirmation"),
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control last',
                                }),
                                help_text=_("Enter the same password as above, for verification."))

    class Meta(BaseRegistrationForm.Meta):
        #Preparing vars to add the new user
        BASE_REGISTRATION_FIELDS = BaseRegistrationForm.Meta.fields
        model = CustomerUser
        fields = [

        ] + BASE_REGISTRATION_FIELDS


