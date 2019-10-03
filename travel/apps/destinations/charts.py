import json
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from apps.destinations.models import (
    Booking,
    Destination,
)
from django.db.models import Count
from django.shortcuts import render


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
    return render(request, 'dashboard/index.html')
