import logging

from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.mail import mail_managers
from django.forms.forms import BaseForm
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView
from django.views.i18n import set_language
from django_registration.backends.activation.views import RegistrationView, ActivationView

from apps.landing_page.models import Plan
from django.shortcuts import render

from apps.accounts.forms import (
    RegistrationForm,
    CustomPasswordResetForm,
    PasswordResetConfirmForm,
    CustomPasswordChangeForm,
    CustomerUserChangeForm,
    CustomAuthenticationForm,
)

from apps.accounts.models import CustomerUser
from apps.payments.paypal.views import SubscriptionView
from config.settings import local as settings

logger = logging.getLogger(__name__)

class RegisterView(SubscriptionView, RegistrationView):
    #email_body_template = 'accounts/registration/activation_email_body.html'
    #html_email_template_name = 'accounts/registration/activation_email_body.html'
    #email_subject_template = 'accounts/registration/activation_email_subject.txt'
    #success_url = reverse_lazy('accounts:register-complete')
    #disallowed_url = reverse_lazy('accounts:django_registration_disallowed')
    template_name = 'accounts/registration/register_form.html'
    #form_class = RegistrationForm

