from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.static import static
from apps.landing_page.views import (
    CategoriesView,
    DetailDestinationView,
    SaveSearchView,
    DeleteRegisterView,
    PrivacySettingView,
    getItineraryPDF,
    ContactUs,
)

from apps.destinations.views.booking import BookingSaveView
from django.contrib.auth.decorators import login_required
from django.conf.urls import (
    handler400,
    handler403,
    handler404,
    handler500
)


#import notifications.urls

admin.autodiscover()

urlpatterns = [
    url(
        r'^sitemap\.xml$',
        sitemap,
        {'sitemaps': {'cmspages': CMSSitemap}},
    ),

    url(
        r'^rosetta/',
        include('rosetta.urls'),
    ),

    path(
        'api/',
        include('apps.api.urls', namespace='api'),
    ),

    path(
        'ratings/',
        include('star_ratings.urls', namespace='ratings')
    ),
]

urlpatterns += i18n_patterns(
    url(
        r'^nested_admin/',
        include('nested_admin.urls'),
    ),

    url(
        r'^admin/',
        admin.site.urls,
    ),

    url(
        r'^impersonate/',
        include('impersonate.urls'),
    ),

    path(
        'summernote/',
        include('django_summernote.urls'),
    ),

    url(
        r'^accounts/',
        include("apps.accounts.urls", namespace='accounts'),
    ),

    path(
        'directmessages/',
        include("apps.directmessages.urls")
    ),

    url(
        r'^category/destination/(?P<slug>\w+)',
        DetailDestinationView.as_view(),
        name='view_detail_destination',
    ),

    url(
        r'^search/',
        CategoriesView.as_view(),
        name='search_category',
    ),

    url(
        r'^category/(?P<alias>\w+)',
        CategoriesView.as_view(),
        name='view_category',
    ),

    path(
        'community/',
        include('apps.community.urls'),
        name='community',
    ),

    path(
        'paypal/',
        include('apps.payments.paypal.urls'),
    ),

    path(
        'dashboard/',
        include("apps.destinations.urls",
                namespace='dashboard'),
    ),

    path(
        'advertisements/',
        include("apps.advertisements.urls",
                namespace='advertisements'),
    ),

    path(
        'personal-search/',
        SaveSearchView.as_view(),
        name='personal-search',
    ),

    path(
        'make-booking/',
        BookingSaveView.as_view(),
        name='make-booking',
    ),

    path(
        'delete-register/',
        DeleteRegisterView.as_view(),
        name='delete-register',
    ),

    path(
        'setting-privacy/',
        PrivacySettingView.as_view(),
        name='setting-privacy',
    ),

    url(r'^get-itinerary/(?P<slug>\w+)',
        getItineraryPDF.as_view(),
        name='get_itinerary'),

    url(r'contact-us',
        ContactUs.as_view(),
        name='contact-us'),

    url(
        r'^',
        include('cms.urls'),
        name='index',
    ),

    #url('^inbox/notifications/',
    #    include(notifications.urls, namespace='notifications')),


)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom Defaults Pages https://docs.djangoproject.com/en/2.1/ref/views/#error-views
handler400 = 'apps.landing_page.views.pag_400_bad_request'
handler403 = 'apps.landing_page.views.pag_403_permission_denied'
handler404 = 'apps.landing_page.views.pag_404_page_not_found'
handler500 = 'apps.landing_page.views.pag_500_server_error'
