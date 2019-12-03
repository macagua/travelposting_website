from django.shortcuts import render
from django.views.generic import (
    DetailView,
    UpdateView,
    View,
)


class CommmunityView(View):
    """
        Vista para pagina comunidad
    """

    def get(self, request, *args, **kwargs):
        return render(request, 'community.html')

class LoginCommunity(View):
    """
        Login para los usuarios de la comunidad
    """

    def get(self, request, *args, **kwargs):
        return render(request, 'community/registration/login.html')


class signupCommunity(View):
    """
        Login para los usuarios de la comunidad
    """

    def get(self, request, *args, **kwargs):
        return render(request, 'community/registration/signup.html')


class ForgetPasswordCommunity(View):
    """
        Login para los usuarios de la comunidad
    """

    def get(self, request, *args, **kwargs):
        return render(request, 'community/registration/forget_password.html')
