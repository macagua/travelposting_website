from django.urls import path
from apps.accounts import views
from django.contrib.auth.views import logout_then_login


app_name = 'accounts'

urlpatterns = [
    path(
        'activate/complete/',
        views.isuccess,
         name='activate-complete',
    ),

    path(
        'activate/<str:activation_key>/',
        views.ActivateAccountView.as_view(),
        name='activate',
    ),

    path(
        'register/',
        views.RegisterView.as_view(),
        name='register',
    ),

    path(
        'login/',
        views.LoginView.as_view(),
        name='login',
    ),

    path(
        'logout/',
        logout_then_login,
        name='logout',
    ),

    path(
        'register/success/',
        views.isuccess,
        name='register-complete',
    ),

    path(
        'password_reset/',
        views.password,
        name='password-reset',
    ),

    path(
        'password_reset/success/',
        views.passwordsuccess,
        name='password-reset-complete',
    ),

    path(
        'password_reset/confirm/',
        views.passwordconfirm,
        name='password-reset-success',
    ),

    path(
        'password_reset/done/',
        views.passworddone,
        name='password-reset-done',
    ),
]
