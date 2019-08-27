import logging
from typing import Any

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.views.generic import RedirectView
from django import http

from apps.accounts.models import CustomerUser
from apps.payments.models.paypal import Coupon
from apps.payments.paypal.resources import Subscription

logger = logging.getLogger(__name__)


class SubscriptionView(object):
    subscription_class = Subscription
    cancel_url = reverse_lazy('paypal:subscription-cancel')
    approved_url = reverse_lazy('paypal:subscription-approved')

    def get_subscription_data(self, form):
        return {
            'plan_id': self.get_plan_id(form),
            'start_time': (timezone.now() + timezone.timedelta(minutes=5)).strftime('%Y-%m-%dT%H:%M:%SZ'),
            'quantity': 1,
            'subscriber': {
                'name': {
                    'given_name': form.cleaned_data.get('first_name'),
                    'surname': form.cleaned_data.get('last_name'),
                },
                'email_address': form.cleaned_data.get('email'),
                'shipping_address': {
                    'name': {
                        'full_name': f"{form.cleaned_data.get('first_name')} {form.cleaned_data.get('last_name')}"
                    },
                    'address': {
                        'address_line_1': form.cleaned_data.get('business_address'),
                        'address_line_2': '',
                        'admin_area_1': 'US',
                        'postal_code': form.cleaned_data.get('postal_code'),
                        'admin_area_2': form.cleaned_data.get('state'),
                        'country_code': 'US'
                    }
                }
            },
            'auto_renewal': True,
            'application_context': {
                'brand_name': 'Travel And Solutions',
                'locale': self.request.LANGUAGE_CODE,
                'shipping_preference': 'NO_SHIPPING',
                'user_action': 'SUBSCRIBE_NOW',
                'payment_method': {
                    'payer_selected': 'PAYPAL',
                    'payee_preferred': 'IMMEDIATE_PAYMENT_REQUIRED'
                },
                'return_url': f"{self.request.scheme}://{self.request.get_host()}{self.approved_url}",
                'cancel_url': f"{self.request.scheme}://{self.request.get_host()}{self.cancel_url}"
            },
            'shipping_amount': {
                'currency_code': 'EUR',
                'value': '0.00'
            }
        }

    def get_plan_id(self, form):
        code = form.cleaned_data.get('coupon')

        if code:
            try:
                coupon = Coupon.objects.get(code=code)
            except Coupon.DoesNotExist:
                print('Invalid coupon')
            else:
                return coupon.plan.paypal_id
        else:
            return form.cleaned_data.get('plan').paypal_id

    def form_valid(self, form):
        sub = self.subscription_class(self.get_subscription_data(form))
        if sub.create():
            logger.debug(f'Created subscription successfully wit id: {sub.id}.')
            new_user = self.register(form)
            new_user.subscription_id = sub.id
            new_user.save()
            for link in sub.links:
                if link.rel == 'approve':
                    return redirect(link.href)
        else:
            form.add_error(None, _(f'The payment could not be processed {sub.error}.'))
            return self.form_invalid(form)


class CancelRedirectView(RedirectView):
    permanent = True
    url = reverse_lazy('accounts:register')

    def get(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:
        subscription_id = request.GET.get('subscription_id')

        try:
            user = CustomerUser.objects.get(subscription_id=subscription_id)
        except CustomerUser.DoesNotExist:
            return http.HttpResponseBadRequest('User not found')
        else:
            user.delete()
        return super(CancelRedirectView, self).get(request, *args, **kwargs)


class ApproveRedirectView(RedirectView):
    permanent = True
    url = reverse_lazy('accounts:register-complete')
