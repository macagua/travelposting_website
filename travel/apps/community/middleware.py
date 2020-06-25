from django.conf import settings
from django.shortcuts import  redirect

class CampaignMiddleware:
    def __init__(self, get_response):
        self.campaign_ref_code = settings.CAMPAIGN_REF_CODE if  hasattr(settings, 'CAMPAIGN_REF_CODE') else 'TPCW-20'
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_view(self, request, view_func, *args, **kwargs):
        if not request.user.is_superuser and request.resolver_match.url_name != 'user-complete-profile' and request.user.is_active and request.user.user.referredBy.ref_code == self.campaign_ref_code and request.user.get_full_name() == '' :
            return redirect('accounts:user-complete-profile', request.user.id)
        return None
