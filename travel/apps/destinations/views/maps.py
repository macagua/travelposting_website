import logging
from django.http import JsonResponse
from django.shortcuts import (
    render,
)
from apps.destinations.forms import DestinationMapForm

from apps.destinations.models import DestinationMap
from django.views.generic import (
    View,
)
from apps.destinations.serializers import (
    MapSerializer,
)

logger = logging.getLogger(__name__)

class DestinationMapView(View):
    def get(self, request):
        form_map =  DestinationMapForm()
        return render(request,'destinations/map/maps.html',{'form_map':form_map})




class MapListView(View):

    def get(self, request):
        if request.is_ajax():
            if 'destiny' in request.GET:
                maps = DestinationMap.objects.all() \
                .filter(destination__user=request.user.id) \
                .filter(destination= request.GET['destiny'])
                return JsonResponse(
                    MapSerializer(maps),
                    safe=False,
                    )
            else:
                return JsonResponse({},
                    safe=False,
                    )
