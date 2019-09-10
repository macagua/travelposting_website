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


class LoginView(auth_views.LoginView):
    template_name = 'accounts/registration/login.html'



class RegisterView(SubscriptionView, RegistrationView):
    email_body_template = 'accounts/registration/activation_email_body.html'
    html_email_template_name = 'accounts/registration/activation_email_body.html'
    email_subject_template = 'accounts/registration/activation_email_subject.txt'
    success_url = reverse_lazy('accounts:register-complete')
    disallowed_url = reverse_lazy('accounts:django_registration_disallowed')
    template_name = 'accounts/registration/register_form.html'
    form_class = RegistrationForm

    def send_activation_email(self, user):
        html_email = None
        activation_key = self.get_activation_key(user)
        context = self.get_email_context(activation_key)
        context['user'] = user
        subject = loader.render_to_string(self.email_subject_template, context, request=self.request)
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())
        body = loader.render_to_string(self.email_body_template, context)

        if self.html_email_template_name is not None:
            html_email = loader.render_to_string(self.html_email_template_name, context)

        user.email_user(subject, body, settings.DEFAULT_FROM_EMAIL, html_message=html_email)

        if not settings.DEBUG:
            self.send_notify_managers_email(user)

    def send_notify_managers_email(self, user):
        context = {
            'user': user
        }
        subject = loader.render_to_string('accounts/registration/notify_register_admin_subject.html', context)
        subject = ''.join(subject.splitlines())
        html_body = loader.render_to_string('accounts/registration/notify_register_admin_body.html', context)
        mail_managers(subject, 'Nuevo usuario registrado', html_message=html_body)

