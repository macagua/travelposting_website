from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder
from django.core.mail import mail_managers, send_mail
from django.db.models import Count, Max, F
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    View
)

from apps.accounts.models import CustomerUser, LastVisitIP
from apps.destinations.models import (
    Booking,
    Destination,
    DestinationVisitor
)

import json
import pycountry



def BookingCharts(request):
    """
        Function to return the data for chars about booking stats.
    """
    query = Booking.objects.filter(destination__user=request.user)\
        .values_list('destination__name')\
        .annotate(dcount=Count('id')
    )

    data = json.dumps(list(query), cls=DjangoJSONEncoder)
    return HttpResponse(data, content_type='application/json')


def DestinationCharts(request):
    """
        Function to return the data for chars about destination stats.
    """
    query = Destination.objects.filter(user=request.user)\
        .values_list('is_published')\
        .annotate(dcount=Count('is_published')
    )

    data = json.dumps(list(query), cls=DjangoJSONEncoder)
    return HttpResponse(data, content_type='application/json')


def DashboardIndex(request):
    """
        Function to render the charts in template.
    """
    statis_destinies = Destination.objects \
                    .filter(user = request.user)\
                    .prefetch_related('visitor') \
                    .annotate(visitor_count = Count('visitor__destination')) \
                    .annotate(last_visit = Max('visitor__date_time')) \
                    .annotate(date_time=F('last_visit')) \
                    .order_by('-visitor_count')

    last_visits = CustomerUser.objects.all().exclude(last_ip=None).values('last_ip', 'location',)[:8]
    only_location = list(set(map(lambda x: x['location'] != None and x['location'] or 'Unknown', last_visits)))
    location ={}
    location.update({visit['location']: { 'visits': visit['visits'], 'code': pycountry.countries.search_fuzzy(visit['location'])[0].alpha_2} for visit in  LastVisitIP.objects.filter(location__in=only_location).values('location').annotate(visits=Count('location'))})

    return render(request, 'dashboard/index.html', {
        'statis_destinies':statis_destinies,
        'last_visits': last_visits,
        'visits_counter': location
        })
