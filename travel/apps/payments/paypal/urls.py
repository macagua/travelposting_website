from django.urls import path

from apps.payments.paypal.views import CancelRedirectView, ApproveRedirectView

app_name = 'paypal'
urlpatterns = [
    path(
        'subscription/approved',
        ApproveRedirectView.as_view(),
        name='subscription-approved',
    ),

    path(
        'subscription/cancel',
        CancelRedirectView.as_view(),
        name='subscription-cancel',
    ),

]
