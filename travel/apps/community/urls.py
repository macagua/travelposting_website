from django.urls import path
from django.contrib.auth.views import logout_then_login

from apps.community.views import CommmunityView, LoginCommunity

urlpatterns = [
    path('', CommmunityView.as_view(), name='index'),
    path(
        'login/',
        LoginCommunity.as_view(),
        name='login-community',
    ),
]
