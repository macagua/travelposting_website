from django.shortcuts import render, redirect
from django.db.models import  Max, Min
from django.views import View
from django.utils.translation import gettext_lazy as _
from django.core.mail import mail_managers
from django.template.loader import render_to_string
from apps.destinations.models import (
    Destination,
    Categorie,
    GeneralDetail,
    SearchLanding
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
            destination_for_category = Destination.objects.filter(is_deleted=False, is_published=True)
            all_categories = True
            categorie = Categorie.objects.all()
        else:
            destination_for_category = Destination.objects.filter(categorie__alias=kwargs.get('alias'), is_deleted=False, is_published=True)
            categorie = Categorie.objects.filter(alias=kwargs.get('alias'))
            all_categories = False
        range_min = GeneralDetail.objects.all().aggregate(Min('regular_price'))
        range_max = GeneralDetail.objects.all().aggregate(Max('regular_price'))
        return render(request, 'services/destination/destinations_for_categorie.html',{
            'all_categories': all_categories,
            'lista_destinos':destination_for_category,
            'active_alias':kwargs.get('alias'),
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


class SaveSearchView(View):
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        country = request.POST.get('city')
        email = request.POST.get('email')
        whatsapp = request.POST.get('whatsapp')

        SearchLanding.objects.create(
            names = name,
            country = country,
            email = email,
            whatsapp = whatsapp
        )


        subject = _('New registered search')

        ctx = {
                    'name': name,
                    'email': email,
                    'country': country,
                    'whatsapp':whatsapp
                }

        html_message = render_to_string(
            'pages/email_feedback.html',
            context=ctx
        )

        message = _(f'A person has done a new search, please review Mr.\'s {name} incoming application. \n Search \
                    the country or city: {country} \n Email:  {email} \n  Whatsapp: {whatsapp} \n or if you want see the \
                    admin site https://travelposting.com/admin/ ')

        mail_managers(subject,
                    message,
                    fail_silently=True,
                    html_message=html_message
                )

        return render(request, 'pages/safeSearch.html')
