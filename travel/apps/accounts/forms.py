from django import forms
from django.utils.translation import gettext_lazy as _, check_for_language
from django_registration.forms import RegistrationForm as BaseRegistrationForm
from apps.accounts.models import CustomerUser
from apps.landing_page.models import Plan
#from tour.payments.paypal.resources import Subscription
from apps.payments.models.paypal import Coupon
from apps.utils.forms import BaseBootstrapForm, FieldKwargsMeta
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordResetForm,
    SetPasswordForm,
    PasswordChangeForm,
)


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



class CustomAuthenticationForm(BaseBootstrapForm, AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)

        self.error_messages.update({'payment_invalid': _('Your account is blocked due to non-payment')})

    """
    def confirm_login_allowed(self, user: AbstractBaseUser) -> None:
        super(CustomAuthenticationForm, self).confirm_login_allowed(user)

        sub = Subscription.find(user.subscription_id)
        if not user.is_staff and not sub.is_active:
            raise forms.ValidationError(
                self.error_messages['payment_invalid'],
                code='payment_invalid'
            )
    """


class RegistrationForm(FieldKwargsMeta, BaseBootstrapForm, BaseRegistrationForm):
    password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput(attrs={
            'class':'form-control first',
        }),
        help_text = _('Use at least 8 characters. Do not use a password from another site or a term that is too obvious, such as your pet\'s name.'))

    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={
            'class':'form-control last',
        }),
        help_text = _("Enter the same password as above, for verification."))

    class Meta(BaseRegistrationForm.Meta):
        #Preparing vars to add the new user
        BASE_REGISTRATION_FIELDS = BaseRegistrationForm.Meta.fields
        model = CustomerUser
        fields = [
                    'plan',
                    'coupon',
                    'first_name',
                    'last_name',
                ] + BASE_REGISTRATION_FIELDS

        fields_kwargs = {
            'plan': {
                'queryset': Plan.objects.filter(active=True),
                'empty_label': _('Select a plan')
            }
        }

    def clean_coupon(self) -> str:
        coupon = self.cleaned_data.get('coupon')

        if coupon:
            if not Coupon.objects.filter(code=coupon).exists():
                raise forms.ValidationError(_('Invalid coupon'), code='invalid_coupon')

            # validar numero de coupones
            # validar que no esté vencido
        return coupon


class CustomPasswordResetForm(BaseBootstrapForm, PasswordResetForm):
    pass


class PasswordResetConfirmForm(BaseBootstrapForm, SetPasswordForm):
    pass


class CustomPasswordChangeForm(BaseBootstrapForm, PasswordChangeForm):
    pass


class CustomerUserChangeForm(BaseBootstrapForm, forms.ModelForm):
    class Meta:
        model = CustomerUser
        fields = (
            'avatar',
            'first_name',
            'last_name',
            'ref_code',
            'business_name',
            'business_address',
            'business_position',
            'postal_code',
            'state',
            'country',
            'language',
            'degree',
            'phone',
            'mobile',
            'web_site',
            'facebook',
            'instagram',
            'twitter',
            'linkedin',
        )

    def clean_language(self):
        lang = self.cleaned_data.get('language')

        if not (lang and check_for_language(lang)):
            forms.ValidationError(_("Non-Permitted Language"))
        return lang
