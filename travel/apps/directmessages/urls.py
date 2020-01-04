from django.urls import path
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import include, url

from apps.directmessages.views import (
    sendViews,
)


urlpatterns = [
    path(
        'send/',
        sendViews.as_view(),
        name='send-messages',
    ),
]
