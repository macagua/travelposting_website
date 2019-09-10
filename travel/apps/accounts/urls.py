from django.contrib.auth.views import logout_then_login
from django.urls import path, include
from django.views.generic import TemplateView

from apps.accounts import views

from django.contrib.auth.views import logout_then_login
from django.urls import path, include
from django.views.generic import TemplateView

from apps.accounts import views

app_name = 'accounts'
urlpatterns = [
    
    path('register/<int:pk>', views.RegisterView.as_view()),    

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
    path('register/success/', views.isuccess),
    path(
        'password_reset/',
        views.password,
        name='password-reset',
    ),


]
