from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone
from django.db.models import  Max, Min
from django.views import View
from django.utils.translation import get_language, gettext_lazy as _
from django.core.mail import mail_managers
from django.template.loader import render_to_string
from django.conf import settings
from apps.destinations.models import (
    Destination,
    Categorie,
    GeneralDetail,
    SearchLanding,
    DestinationMap
)
from apps.destinations.utils import get_client_ip
from apps.accounts.models import Comment
from apps.landing_page.forms import ContactUsForm
from apps.landing_page.models import DeleteReg, PrivacySetting
from easy_pdf.views import PDFTemplateView



class CategoriesView(View):
    """
        Vista para categorias
    """
    def get_filter_query(self, request):
        query_base = Q(is_deleted=False, is_published=True)

        if "nameDestination" in request.GET and request.GET['nameDestination'] != "":
            query_base&= Q(name__contains=request.GET['nameDestination'])
            return query_base

        if "minPrice" in request.GET and request.GET['minPrice'] != "" and "maxPrice" in request.GET and request.GET['maxPrice'] != "":
            query_base|= Q(details__general__regular_price__range=[request.GET['minPrice'],request.GET['maxPrice']])
            return query_base

        if "added" in request.GET  and request.GET['added']!="":
            if request.GET['added'] == "24hrs":
                time_ago = timezone.now()-timezone.timedelta(hours=24)

            if request.GET['added'] == "lastWeek":
                time_ago = timezone.now()-timezone.timedelta(days=7)

            if request.GET['added'] == "anytime":
                time_ago =timezone.now()

            query_base|= Q(updated_at__gte=time_ago, updated_at__lte=timezone.now())
            return query_base

        if "category" in request.GET  and request.GET['category'] != "" and request.GET['category'] != "all":
            query_base&= Q(categorie__alias=request.GET['category'])
            return query_base

    def get(self, request, *args, **kwargs):
        if  request.resolver_match.url_name =="search_category":
            all_categories = True
            categorie = Categorie.objects.all()
            filter_category = Destination.objects.filter(self.get_filter_query(request))
        else:
            if kwargs.get('alias') == 'all':
                filter_category = Destination.objects.filter(is_deleted=False, is_published=True)
                all_categories = True
                categorie = Categorie.objects.all()
            else:
                filter_category = Destination.objects.filter(categorie__alias=kwargs.get('alias'), is_deleted=False, is_published=True)
                categorie = Categorie.objects.filter(alias=kwargs.get('alias'))
                all_categories = False
        
        # Mostrar solo las que tengan name en el idioma seleccionado
        language_filter = {'name_%s' % get_language(): None}
        filter_category = filter_category.exclude(**language_filter)

        range_min = GeneralDetail.objects.all().aggregate(Min('regular_price'))
        range_max = GeneralDetail.objects.all().aggregate(Max('regular_price'))
        paginator = Paginator(filter_category, 8)
        page = request.GET.get('page')
        lista_destinos = paginator.get_page(page)
        return render(request, 'services/destination/destinations_for_categorie.html',{
            'all_categories': all_categories,
            'lista_destinos':lista_destinos,
            'active_alias':kwargs.get('alias'),
            'categorie':categorie,
            'range_min':range_min,
            'range_max':range_max
            })

class DetailDestinationView(View):
    def get(self, request, *args, **kwargs):
        destination= get_object_or_404(Destination, id=kwargs.get('slug'))
        key = settings.GOOGLE_MAPS_API_KEY
        comment = Comment.objects.filter(post=kwargs.get('slug')).order_by('-created')[0:3]

        try:
            destino_map = DestinationMap.objects.get(destination_id=kwargs.get('slug'))
            return render(request, 'services/destination/detail_destination.html',{
                'destino':destination,
                'map': destino_map,
                'key': key,
                'comment': comment,
            })
        except:
            data = _("Don't have exist map yet!")
            return render(request, 'services/destination/detail_destination.html',{
                'destino':destination,
                'data': data,
                'key': key,
                'comment': comment,
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


class DeleteRegisterView(View):
    def post(self, request, *args, **kwargs):
        first_name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        agree = request.POST.get('check')

        if agree==None:
            agree = False
        else:
            agree = True

        DeleteReg.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            agree = agree
        )


        subject = _('New request for delete')

        ctx = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'agree':agree
                }

        html_message = render_to_string(
            'pages/request_delete_feedback.html',
            context=ctx
        )

        message = _(f'if you want see the \
                    admin site https://travelposting.com/admin/ ')

        mail_managers(subject,
                    message,
                    fail_silently=True,
                    html_message=html_message
                )

        return render(request, 'pages/request.html')

class ContactUs(View):
    def post(self,request):
        updated_data = request.POST.copy()
        updated_data.update({'ip_client': get_client_ip(request)})
        form = ContactUsForm(updated_data)
        if form.is_valid() == False:
            subject = _('You have a new contact')
            ctx = {
                'user' : request.POST.get('email'),
                'message': request.POST.get('message')
            }

            html_message = render_to_string(
                'dashboard/dashboard_email.html',
                context=ctx
            )

            message = _(f'if you want see the admin site https://travelposting.com/admin/')

            mail_managers(subject,
                        message,
                        fail_silently=True,
                        html_message=html_message
                    )

            messages.success(request, _('Thank you very much for contacting us, we will be responding very soon '), extra_tags='success_contact_us')
            #form.save()
        else:
            messages.error(request, _('A error has ocurred while processing your message'), extra_tags='danger')
            print(form.errors)
        return redirect('/')

class PrivacySettingView(View):
    def post(self, request, *args, **kwargs):
        cookie = request.POST.get('cookie')
        ganality = request.POST.get('ganality')
        facebook = request.POST.get('facebook')
        twitter = request.POST.get('twitter')
        pinteres = request.POST.get('pinterest')

        if cookie=='Yes':
            cookie = True
        else:
            cookie = False

        if ganality=='Yes':
            ganality = True
        else:
            ganality = False

        if facebook=='Yes':
            facebook = True
        else:
            facebook = False

        if twitter=='Yes':
            twitter = True
        else:
            twitter = False

        if pinteres=='Yes':
            pinteres = True
        else:
            pinteres = False

        PrivacySetting.objects.create(
            ip = request.META.get('REMOTE_ADDR'),
            cookie = cookie,
            facebook = facebook,
            twitter = twitter,
            pinteres = pinteres,
        )


        subject = _('New privacity request.')

        ctx = {
            'ip' : request.META.get('REMOTE_ADDR'),
            'cookie' : cookie,
            'facebook' : facebook,
            'twitter' : twitter,
            'pinterest' : pinteres,
        }

        html_message = render_to_string(
            'pages/request_form_feedback.html',
            context=ctx
        )

        message = _(f'if you want see the \
                    admin site https://travelposting.com/admin/ ')

        mail_managers(subject,
                    message,
                    fail_silently=True,
                    html_message=html_message
                )

        return render(request, 'pages/request.html')


class getItineraryPDF(PDFTemplateView):
    template_name = 'pdf/itinerary.html'
    download_filename = 'intinerary.pdf'

    def get_context_data(self, **kwargs):
        try:
            return super(getItineraryPDF, self).get_context_data(
                destino = Destination.objects.get(id=kwargs.get('slug')),
                pagesize='letter',
                title=_('Itinerary'),
                **kwargs
            )
        except:
            context = super(getItineraryPDF, self).get_context_data(**kwargs)

            return context


