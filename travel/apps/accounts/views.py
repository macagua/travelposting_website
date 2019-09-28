import logging
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.accounts.models import CustomerUser
from apps.payments.paypal.views import SubscriptionView
from config.settings import local as settings
from django.core.exceptions import PermissionDenied
from django.core.mail import mail_managers
from django.forms.forms import BaseForm
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.shortcuts import (
    render,
    redirect,
    reverse,
)
from django.views.generic import (
    DetailView,
    UpdateView,
    View,
)
from django.views.i18n import set_language
from django_registration.backends.activation.views import RegistrationView, ActivationView
from apps.landing_page.models import Plan
from django.shortcuts import render
from apps.accounts.forms import (
    SignInForm,
    RegistrationForm,
    CustomPasswordResetForm,
    PasswordResetConfirmForm,
    CustomPasswordChangeForm,
    CustomerUserChangeForm,
    CustomAuthenticationForm,
)
from django.contrib.auth import authenticate, login

logger = logging.getLogger(__name__)


class LoginView(View):
    template_name = 'accounts/registration/login.html'
    form = SignInForm

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name,
            {'form': self.form},
        )

    def post(self, request, *args, **kwargs):
        user = request.POST.get('email')
        password = request.POST.get('password')
        import ipdb; ipdb.set_trace()
        user = authenticate(username=user, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse('destinations:list'))
        else:
            errors = 'Ha ocurrido un error, Usuario o Contraseña Incorrecta.'

            return render(
                request,
                self.template_name,
                {'form': self.form, 'errors':errors},
            )


class RegisterView(SubscriptionView, RegistrationView):
    email_body_template = 'accounts/registration/activation_email_body.html'
    html_email_template_name = 'accounts/registration/activation_email_body.html'
    email_subject_template = 'accounts/registration/activation_email_subject.txt'
    success_url = reverse_lazy('accounts:register-complete')
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

        if settings.DEBUG:
            self.send_notify_managers_email(user)

    def send_notify_managers_email(self, user):
        context = {
            'user': user
        }
        subject = loader.render_to_string('accounts/registration/notify_register_admin_subject.html', context)
        subject = ''.join(subject.splitlines())
        html_body = loader.render_to_string('accounts/registration/notify_register_admin_body.html', context)
        mail_managers(subject, 'Nuevo usuario registrado', html_message=html_body)


def isuccess(request):
    return render(request, 'accounts/registration/succes_register.html')

class ActivateAccountView(ActivationView):
    success_url = reverse_lazy('accounts:activate-complete')
    template_name = 'accounts/registration/activation_failed.html'

def password(request):
    return render(request, 'accounts/registration/forgot_password.html')


def passwordsuccess(request):
    return render(request, 'accounts/registration/forgot_password_success.html')


def passwordconfirm(request):
    return render(request, 'accounts/registration/password_reset_confirm.html')


def passworddone(request):
    return render(request, 'accounts/registration/password_reset_done.html')


class PasswordResetView(auth_views.PasswordResetView):
    email_template_name = 'accounts/registration/password_reset_email.html'
    html_email_template_name = 'accounts/registration/password_reset_email.html'
    template_name = 'accounts/registration/password_reset_form.html'
    success_url = reverse_lazy('accounts:password-reset-done')
    form_class = CustomPasswordResetForm


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'accounts/registration/password_reset_done.html'


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/registration/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password-reset-complete')
    form_class = PasswordResetConfirmForm


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/registration/password_reset_complete.html'


class CustomUserDetailView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/user/_detail.html'
    model = CustomerUser


class CustomUserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'accounts/user/_form.html'
    model = CustomerUser
    form_class = CustomerUserChangeForm

    def form_valid(self, form: BaseForm) -> HttpResponse:
        super(CustomUserUpdateView, self).form_valid(form)
        return set_language(self.request)


class PasswordChangeView(LoginRequiredMixin, auth_views.PasswordChangeView):
    template_name = 'accounts/user/password_change.html'
    success_url = reverse_lazy('accounts:password-change-done')
    form_class = CustomPasswordChangeForm


class PasswordChangeDoneView(LoginRequiredMixin, auth_views.PasswordChangeDoneView):
    template_name = 'accounts/user/password_change_done.html'
