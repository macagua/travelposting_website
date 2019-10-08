import logging
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.http import JsonResponse
from django.http import QueryDict
from django.shortcuts import (
    render,
    get_object_or_404,
)
from apps.destinations.forms import DestinationMapForm

from apps.destinations.models import DestinationMap
from django.views.generic import (
    View,
)
from apps.destinations.serializers import (
    MapSerializer,
    mapped_errors_form,
)

logger = logging.getLogger(__name__)

class DestinationMap(View):
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
					MapsSerializer(itinerary),
					safe=False,
					)
			else:
				return JsonResponse({},
					safe=False,
					)
