import logging
from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _
from django.shortcuts import (
    render,
    get_object_or_404,
)
from django.http import QueryDict
from apps.destinations.forms import DestinationMapForm

from apps.destinations.models import Destination, DestinationMap
from django.views.generic import (
    View,
)
from apps.destinations.serializers import (
    MapSerializer,
    mapped_errors_form,
)

from apps.utils.mixins import NoCommunityRequiredMixin

logger = logging.getLogger(__name__)

class DestinationMapView(NoCommunityRequiredMixin, View):
    def get(self, request):
        form_map =  DestinationMapForm()
        form_map.fields['destination'].queryset = Destination.objects.filter(
                user=request.user,
                map=None)
        destination = DestinationMap.objects.filter(destination__user=request.user.id)
        return render(request,'destinations/map/maps.html',{'form_map':form_map, 'destination':destination})

    def post(self,request):
        form_map = DestinationMapForm(request.POST)
        if form_map.is_valid():
            if form_map.save() :
                destination = DestinationMap.objects.filter(destination__user=request.user.id)
                return render(request,'destinations/map/maps.html',{'form_map':form_map, 'destination':destination})
        else:
            return JsonResponse(
                {
                'error':mapped_errors_form(form_map),
                'status':False
                },
                safe=False,
            )

    def delete(self,request):
        pk_map= QueryDict(request.body)
        maps = get_object_or_404(DestinationMap, pk=pk_map['pk'])
        if maps.delete() :
            return JsonResponse(
                {
                'status':True
                },
                safe=False,
            )


class MapListView(View):
    def get(self, request):
        if request.is_ajax():
            if 'destiny' in request.GET:
                maps = DestinationMap.objects.all() \
                .filter(destination__user=request.user.id) \
                .filter(destination=request.GET['destiny'])
                return JsonResponse(
                    MapSerializer(maps),
                    safe=False,
                    )
            else:
                return JsonResponse({},
                    safe=False,
                    )
