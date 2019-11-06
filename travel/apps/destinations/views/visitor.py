from django.contrib.gis.geoip2 import GeoIP2
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import (
    View,
)
from django.utils.translation import gettext_lazy as _

from apps.destinations.models import (
	Destination,
	DestinationVisitor
)
from apps.destinations.utils import get_client_ip

class VisitorView(View):
    def get(self, request):
    	geo_ip = GeoIP2()
    	if settings.DEBUG :
    		ip_visitor = "72.14.207.99"
    		data_visitor = geo_ip.city(ip_visitor)
    	else:
    		ip_visitor = get_client_ip(request)
    		data_visitor = geo_ip.city(str(ip_visitor))
    	try:
	    	DestinationVisitor.objects.create(
	    		destination = Destination.objects.get(request.GET['destination']),
	    		ip_address  = ip_visitor,
	    		dma_code =data_visitor['dma_code'] ,
	    		country_code = data_visitor['country_code'],
	    		country_name =data_visitor['country_name']
	    	)
	    	return JsonResponse({},safe=False,status=200)
    	except Exception as e:
    		return JsonResponse({},safe=False,status=200)
