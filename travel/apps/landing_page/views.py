from django.shortcuts import render
from django.db.models import  Max, Min
from django.views import View
from apps.destinations.models import (
    Destination,
    Categorie,
    GeneralDetail
)
# Create your views here.

class CommmunityView(View):
    """
        Vista para pagina comunidad
    """

    def get(self, request, *args, **kwargs):
        return render(request, 'community.html')


class CategoriesView(View):
    """
        Vista para categorias
    """
    def get(self, request, *args, **kwargs):
        if kwargs.get('alias') == 'all':
            destination_for_category = Destination.objects.all()
            categorie='all'
        else:
            destination_for_category = Destination.objects.filter(categorie__alias=kwargs.get('alias'))
            categorie=Categorie.objects.filter(alias=kwargs.get('alias'))
        range_min = GeneralDetail.objects.all().aggregate(Min('regular_price'))
        range_max = GeneralDetail.objects.all().aggregate(Max('regular_price'))
        return render(request, 'services/destination/destinations_for_categorie.html',{
            'lista_destinos':destination_for_category,
            'categorie':categorie,
            'range_min':range_min,
            'range_max':range_max
            })

class DetailDestinationView(View):
    def get(self, request, *args, **kwargs):
        destination= Destination.objects.get(id=kwargs.get('slug'))
        return render(request, 'services/destination/detail_destination.html',{
            'destino':destination,
            })
