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

    path('register/<valor>/<int>', views.RegisterView.as_view(), name='register2'),

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
        views.PasswordResetView.as_view(),
        name='password-reset',
    ),

    path(
        'reset/<uidb64>/<token>/',
        views.PasswordResetConfirmView.as_view(),
        name='password-reset-confirm',
    ),

    path(
        'password_reset/done/',
        views.PasswordResetDoneView.as_view(),
        name='password-reset-done',
    ),

    path(
        'reset/complete/',
        views.PasswordResetCompleteView.as_view(),
        name='password-reset-complete',
    ),

    path(
        'password_change/',
        views.PasswordChangeView.as_view(),
        name='password-change',
    ),

    path(
        'password_change/done/',
        views.PasswordChangeDoneView.as_view(),
        name='password-change-done',
    ),

    path(
        'user/<int:pk>/details/',
        views.CustomUserDetailView.as_view(),
        name='user-details',
    ),

    path(
        'user/<int:pk>/update/',
        views.CustomUserUpdateView.as_view(),
        name='user-update',
    ),

    path(
        'user/<int:pk>/complete/',
        views.CompleteProfileView.as_view(),
        name='user-complete-profile',
    ),
]
