from django.views.generic import (
    DetailView,
    UpdateView,
    View,
    CreateView,
)
from django.utils.translation import gettext as _
from django_registration.backends.activation.views import RegistrationView, ActivationView
from django.shortcuts import (
    render,
    redirect,
    reverse,
)
from django.urls import reverse_lazy
from .forms import CommunitySignUpForm, SignInForm
from apps.accounts.models import CustomerUser
from django.template import loader
from config.settings import local as settings
from django.core.mail import mail_managers
from django.contrib.auth import authenticate, login



class CommmunityView(View):
    """
        Vista para pagina comunidad
    """

    def get(self, request, *args, **kwargs):
        return render(request, 'community.html')


class LoginCommunity(View):
    template_name = 'community/registration/login.html'
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
        user = authenticate(
            username=user, password=password, is_community=True)

        if user is not None:
            login(request, user)
            return redirect(reverse('community:dashboard-community'))
        else:
            errors = _('An error, Incorrect User or Password has occurred.')

            return render(
                request,
                self.template_name,
                {'form': self.form, 'errors': errors},
            )



class signupCommunity(RegistrationView):
    email_body_template = 'accounts/registration/activation_email_body.html'
    html_email_template_name = 'accounts/registration/activation_email_body.html'
    email_subject_template = 'accounts/registration/activation_email_subject.txt'
    success_url = reverse_lazy('accounts:register-complete')
    template_name = 'community/registration/signup.html'
    form_class = CommunitySignUpForm

    def send_activation_email(self, user):
        html_email = None
        activation_key = self.get_activation_key(user)
        context = self.get_email_context(activation_key)
        context['user'] = user
        subject = loader.render_to_string(
            self.email_subject_template, context, request=self.request)
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())
        body = loader.render_to_string(self.email_body_template, context)

        if self.html_email_template_name is not None:
            html_email = loader.render_to_string(
                self.html_email_template_name, context)

        user.email_user(subject, body, settings.DEFAULT_FROM_EMAIL,
                        html_message=html_email)

        if settings.DEBUG:
            self.send_notify_managers_email(user)

    def send_notify_managers_email(self, user):
        context = {
            'user': user
        }
        subject = loader.render_to_string(
            'accounts/registration/notify_register_admin_subject.html', context)
        subject = ''.join(subject.splitlines())
        html_body = loader.render_to_string(
            'accounts/registration/notify_register_admin_body.html', context)
        mail_managers(subject, 'Nuevo usuario registrado',
                      html_message=html_body)



class ForgetPasswordCommunity(View):
    """
        Login para los usuarios de la comunidad
    """

    def get(self, request, *args, **kwargs):
        return render(request, 'community/registration/forget_password.html')


class DashboardCommunity(View):
    """
        Login para los usuarios de la comunidad
    """

    def get(self, request, *args, **kwargs):
        return render(request, 'community/dashboard/dashboard.html')


