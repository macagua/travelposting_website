# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    print_function,
    unicode_literals,
)
from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.static import static
from apps.landing_page.views import (
    CommmunityView,
    CotegoriesView,
    DetailDestinationView
)
admin.autodiscover()

urlpatterns = [
    url(
        r'^sitemap\.xml$',
        sitemap,
        {'sitemaps': {'cmspages': CMSSitemap}},
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
        'tour/',
        include("apps.destinations.urls", namespace='tours'),
    ),

    path(
        'api/',
        include('apps.api.urls', namespace='api'),
    ),

    url(
        r'^community',
        CommmunityView.as_view(),
    ),
    url(
        r'^cotegory/(?P<alias>\w+)/destination/(?P<slug>\w+)',
        DetailDestinationView.as_view(),
        name='view_detail_destination'
    ),

    url(
        r'^category/(?P<alias>\w+)',
        CotegoriesView.as_view(),
        name='view_category'
    ),

    path(
        'paypal/',
            include('apps.payments.paypal.urls'),
    ),

    url(
        r'^',
        include('cms.urls'),
    ),

)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
