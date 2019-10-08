import logging
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


from django.shortcuts import (
    render,
    get_object_or_404,
)
from apps.destinations.forms import DestinationMapForm
from django.views.generic import (
    View,
)

logger = logging.getLogger(__name__)

class DestinationMap(View):
	def get(self, request):
		form_map =  DestinationMapForm()
		return render(request,'destinations/map/maps.html',{'form_map':form_map})
