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

]
