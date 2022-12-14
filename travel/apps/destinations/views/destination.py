import logging
import datetime as dt
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group
from django.contrib.auth.views import redirect_to_login
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.http import QueryDict
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import never_cache
from django.views.generic.detail import BaseDetailView, SingleObjectMixin
from django.views.generic.edit import BaseCreateView
from django.views.generic.list import MultipleObjectMixin
from django.contrib.auth import password_validation
from django.core import exceptions
from django.db.models import Q # new
from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    ListView,
    UpdateView,
    View,
)
from django.views.generic.edit import ModelFormMixin
from django.shortcuts import (
    render,
    get_object_or_404,
)
from django.template.loader import render_to_string
from django.core.mail import mail_managers
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.utils.datastructures import MultiValueDictKeyError
from apps.accounts.models import CustomerUser




from apps.destinations.forms import (
    AgencyAddForm,
    AgencyEditForm,
    AgencyAddExistingUserForm,
    DestinationForm,
    TourDataForm,
    HeaderSectionInlineForm,
    DestinationDetailForm,
    ItineraryForm,
    RequestForm,
    FileAddForm
)
from apps.destinations.models import (
    Destination,
    TourData,
    HeaderSection,
    DestinationDetail,
    GeneralDetail,
    OptionTabData,
    Itinerary,
    InventarioDetail,
    BookingDetail,
    SocialNetwork,
    MessageDashboard,
    Request,
    File,
)
from apps.destinations.utils import (
    BaseInlineModelFormMixin,
    JSONResponseMixin,
    ModelEncoder,
)

from apps.destinations.serializers import (
    ItinerarySerializer,
    DestinySerializer,
    ItineraryAloneSerializer,
    mapped_errors_form,
)

from apps.utils.mixins  import NoCommunityRequiredMixin

logger = logging.getLogger(__name__)


class DestinationListView(NoCommunityRequiredMixin, ListView):
    template_name = 'destinations/_list.html'
    queryset = Destination.objects.filter(is_deleted=False)

    def get_queryset(self):
        queryset = super(DestinationListView, self).get_queryset()
        return queryset.filter(user=self.request.user)


class BaseDestinationView(NoCommunityRequiredMixin, BaseInlineModelFormMixin):
    template_name = 'destinations/_form.html'
    form_class = DestinationForm
    queryset = Destination.objects.filter(is_deleted=False)
    success_url = reverse_lazy('destinations:list')

    def get_initial(self):
        return {'user': self.request.user}

    def get_inline_tour_data_class(self):
        self.inline_tour_data_class = inlineformset_factory(
            Destination,
            TourData,
            form=TourDataForm,
            # formset=tour_dataInlineFormSet,
            extra=1,
            min_num=0,
            max_num=1,
            validate_max=True,
            validate_min=True
        )

    def get_inline_header_class(self):
        self.inline_header_class = inlineformset_factory(
            Destination,
            HeaderSection,
            form=HeaderSectionInlineForm,
            # formset=headerInlineFormSet,
            extra=1,
            min_num=0,
            max_num=1,
            validate_max=True,
            validate_min=True
        )

    def get_inline_destination_detail_class(self):
        self.inline_destination_detail_class = inlineformset_factory(
            Destination,
            DestinationDetail,
            form=DestinationDetailForm,
            # formset=destination_detailInlineFormSet,
            extra=1,
            min_num=0,
            max_num=1,
            validate_max=True,
            validate_min=True
        )

    def get_context_data(self, **kwargs):
        context = {}

        if 'tour_data_inlineformset' not in kwargs:
            self.get_inline_tour_data_class()
            context['tour_data_inlineformset'] = self.get_form_inline(
                self.inline_tour_data_class)

        if 'header_inlineformset' not in kwargs:
            self.get_inline_header_class()
            context['header_inlineformset'] = self.get_form_inline(
                self.inline_header_class)

        if 'destination_detail_inlineformset' not in kwargs:
            self.get_inline_destination_detail_class()
            context['destination_detail_inlineformset'] = self.get_form_inline(
                self.inline_destination_detail_class)
        context.update(kwargs)
        return super().get_context_data(**context)

    def post(self, request, *args, **kwargs):
        try:
            #Step 1: Saving destination data.
            destination, created = Destination.objects.update_or_create(
                user=CustomerUser.objects.get(id=request.POST.get('user')),
                name=request.POST.get('name'),
            )

            #Set the categories.
            destination.categorie.set(request.POST.get('categorie'))
            destination.short_description=request.POST.get('short_description')
            destination.description=request.POST.get('description')
            destination.departure_date=dt.datetime.strptime(request.POST.get('departure_date'), '%M/%d/%Y') if request.POST.get('departure_date') !='' else None
            destination.departure_time=request.POST.get('departure_time') or None
            destination.arrival_date=dt.datetime.strptime(request.POST.get('arrival_date'), '%M/%d/%Y') if request.POST.get('arrival_date') != '' else None
            destination.arrival_time=request.POST.get('arrival_time') or None
            destination.has_wifi=request.POST.get('has_wifi') or None
            destination.has_breakfast_incluided=request.POST.get('has_breakfast_incluided') or None
            destination.has_gym=request.POST.get('has_gym') or None
            destination.has_air_conditioning=request.POST.get('has_air_conditioning') or None
            destination.has_restaurant=request.POST.get('has_restaurant') or None
            destination.has_bar=request.POST.get('has_bar') or None
            destination.has_housekeeping=request.POST.get('has_housekeeping') or None
            destination.has_room_service=request.POST.get('has_room_service') or None
            destination.has_business_services=request.POST.get('has_business_services') or None
            destination.has_hob_tub=request.POST.get('has_hob_tub') or None
            destination.has_front_desk=request.POST.get('has_front_desk') or None
            destination.has_laundry=request.POST.get('has_laundry') or None
            destination.save()

            #creating the destination detail object.
            detail, created = DestinationDetail.objects.get_or_create(destination=destination)

            #Step 2: Saving DestinationDetail data.
            general_detail, create = GeneralDetail.objects.update_or_create(
                destination_detail=DestinationDetail.objects.get(id=detail.id),
            )

            #Updating necessary fields.
            general_detail.regular_price=request.POST.get('details-0-general-0-regular_price_0')
            general_detail.sale_price=request.POST.get('details-0-general-0-sale_price_0')
            general_detail.date_on_sale_from=request.POST.get('details-0-general-0-date_on_sale_from') or None
            general_detail.date_on_sale_to=request.POST.get('details-0-general-0-date_on_sale_to') or None
            general_detail.status_imp=request.POST.get('details-0-general-0-status_imp')
            general_detail.class_imp=request.POST.get('details-0-general-0-class_imp')
            general_detail.save()

            #Step 3: Saving the Inventario data.
            datedigit = (dt.datetime.now()).strftime('%y')
            count_dest = str(Destination.objects.filter(user=request.POST.get('user')).count())
            sku_destination = (datedigit + '0' + count_dest + destination.name[:4].upper())
            inventario, created = InventarioDetail.objects.update_or_create(
                destination_detail=DestinationDetail.objects.get(id=detail.id),
            )

            #Updating changes and Set the new sku.
            inventario.manager=True if request.POST.get('details-0-inventario-0-manager') == 'on' else False
            inventario.quantity=request.POST.get('details-0-inventario-0-quantity')
            inventario.reserva=request.POST.get('details-0-inventario-0-reserva')
            inventario.umb_exist=request.POST.get('details-0-inventario-0-umb_exist')
            inventario.sold_individually=True if request.POST.get('details-0-inventario-0-sold_individually') == 'on' else False
            inventario.sku=sku_destination
            inventario.save()

            #Step 4: Saving the Booking preference data.
            booking, created = BookingDetail.objects.update_or_create(
                destination_detail=DestinationDetail.objects.get(id=detail.id),
                is_active='1',
            )

            #Updating fields.
            booking.start_date=request.POST.get('details-0-booking-0-start_date') if request.POST.get('details-0-booking-0-start_date') != '' else None
            booking.end_date=request.POST.get('details-0-booking-0-end_date') if request.POST.get('details-0-booking-0-end_date') != '' else None
            booking.days=request.POST.get('details-0-booking-0-days')
            booking.number_ticket=request.POST.get('details-0-booking-0-number_ticket') if request.POST.get('details-0-booking-0-number_ticket') != '' else None
            booking.special_price=request.POST.get('details-0-booking-0-special_price_0') if request.POST.get('details-0-booking-0-special_price') != '' else None
            booking.save()

        except BaseException:
            print("Destination can not be created/updated")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        else:
            return HttpResponseRedirect(self.success_url)


class DestinationCreateView(BaseDestinationView, CreateView):
    extra_context = {
        'submit': _('Add Destination')
    }

    def post(self, request, *args, **kwargs):
        self.object = None
        return super(
            DestinationCreateView, self).post(
            request, *args, **kwargs)


class DestinationUpdateView(BaseDestinationView, UpdateView):
    extra_context = {
        'submit': _('Update Destination')
    }

    def get_form_inline_kwargs(self):
        kwargs = super().get_form_inline_kwargs()

        if hasattr(self, 'object'):
            kwargs.update({
                'instance': self.object
            })
        return kwargs

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        return super().post(request, *args, **kwargs)

    def form_valid(
            self, form, tour_data_inlineformset, header_inlineformset,
            destination_detail_inlineformset):
        self.object = form.save()

        self.inline_tour_data_object = tour_data_inlineformset.save()
        self.inline_header_object = header_inlineformset.save()
        self.inline_destination_detail_object = destination_detail_inlineformset.save()

        return HttpResponseRedirect(self.get_success_url())


class DestinationDetailView(NoCommunityRequiredMixin, DetailView):
    template_name = 'destinations/_details.html'
    queryset = Destination.objects.filter(is_deleted=False)


class DestinationDeleteView(NoCommunityRequiredMixin, DeleteView):
    template_name = 'destinations/_delete.html'
    queryset = Destination.objects.filter(is_deleted=False)
    success_url = reverse_lazy('destinations:list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_deleted = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class OptionTabDataTemplateAjaxView(
        NoCommunityRequiredMixin, JSONResponseMixin, BaseDetailView):
    model = OptionTabData

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(
            context, encoder=ModelEncoder, **response_kwargs)


class GalleryListView(NoCommunityRequiredMixin, SingleObjectMixin, ListView):
    template_name = 'destinations/gallery/_list.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Destination.objects.all())
        return super(GalleryListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GalleryListView, self).get_context_data(**kwargs)
        context['destination'] = self.object
        return context

    def get_queryset(self):
        return self.object.gallery.all()


class VideoListView(NoCommunityRequiredMixin, SingleObjectMixin, ListView):
    template_name = 'destinations/gallery/_list_video.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Destination.objects.all())
        return super(VideoListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(VideoListView, self).get_context_data(**kwargs)
        context['destination'] = self.object
        return context

    def get_queryset(self):
        return self.object.media.all()


class BaseItineraryMixin(object):
    form_class = ItineraryForm
    template_name = 'destinations/itinerary/itinerary_create.html'
    model = Itinerary
    success_url = reverse_lazy('destinations:itinerary-list')

    def get_queryset(self):
        q = super().get_queryset()
        q.filter(destination__user=self.request.user)
        return q

    def get_context_data(self, **kwargs):
        c = super().get_context_data(**kwargs)
        c['destination_list'] = Destination.objects.filter(user=self.request.user)
        return c


class ItineraryCreateView(NoCommunityRequiredMixin, BaseItineraryMixin, CreateView):
    def get_context_data(self, **kwargs):
        c = super().get_context_data(**kwargs)
        c['button_label'] = _('create a new itinerary')
        return c


class ItineraryUpdateView(NoCommunityRequiredMixin, BaseItineraryMixin, UpdateView):
    def get_context_data(self, **kwargs):
        c = super().get_context_data(**kwargs)
        c['button_label'] = _('update itinerary')
        return c


class ItineraryView(View):
    def get(self, request,*args,**kwargs):
        if request.is_ajax():
            if 'q' in request.GET:
                destination = Destination.objects.all() \
                    .filter(user=request.user.id)
                if request.GET['q']!='':
                    destination.filter(name__contains=request.GET['q'])
                return JsonResponse(
                    DestinySerializer(destination),
                    safe=False,
                )
            if 'pk_i' in request.GET:
                itinerary = Itinerary.objects.get(pk=request.GET['pk_i'])
                return JsonResponse({
                    'data':ItineraryAloneSerializer(itinerary),
                    'status':True,
                    },
                    safe=False,
                )

            if 'destiny' in request.GET:
                itinerary = Itinerary.objects.all()\
                            .filter(destination__user=request.user.id)\
                            .filter(destination= request.GET['destiny'])
                return JsonResponse(
                    ItinerarySerializer(itinerary),
                    safe=False,
                )
            else:
                return JsonResponse({},
                    safe=False,
                )
        else:
            c = {}
            itinerary_list = Itinerary.objects.filter(destination__user=request.user)
            destination_list = Destination.objects.filter(user=request.user)
            c['itinerary_list'] = itinerary_list
            c['destination_list'] = destination_list
            c['form'] = ItineraryForm

            return render(
                request,
                'destinations/itinerary/itinerary.html',
                c,
            )

    def post(self,request):
        form_itinerary = ItineraryForm(request.POST)
        if form_itinerary.is_valid():
            if form_itinerary.save() :
                return JsonResponse({'msg':_('A new itinerary item has been registered'),'status':True},
                    safe=False,
                )
        else:
            return JsonResponse(
                {
                'error':mapped_errors_form(form_itinerary),
                'status':False
                },
                safe=False,
            )

    def delete(self,request):
        pk_itinerary= QueryDict(request.body)
        itinerary = get_object_or_404(Itinerary, pk=pk_itinerary['pk'])
        if itinerary.delete() :
            return JsonResponse(
                {
                'status':True
                },
                safe=False,
            )
    def put(self, request):
        updated_data= QueryDict(request.body)
        itinerary = Itinerary.objects.get(pk=updated_data['pk_i'])
        form = ItineraryForm(updated_data, instance=itinerary)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'msg': _('Itinerary information has been updated'),
                'type': 'success',
                'status': True,
            })
        else:
            return JsonResponse({
                'errors': mapped_errors_form(form),
                'status': False,
            })


class SocialNetworkListView(NoCommunityRequiredMixin, SingleObjectMixin, ListView):
    template_name = 'destinations/_socialNetworkList.html'
    success_url = reverse_lazy('destinations:social-network')

    def get(self, request, *args, **kwargs):
        add = SocialNetwork.objects.filter(destination__user=self.request.user)
        destinos = Destination.objects.filter(user=self.request.user)
        return render(request, self.template_name, {'add':add, 'destinos':destinos})

    def post(self, request, *args, **kwargs):
        #Definition of variables that return from the frontend
        use_default_networks = request.POST.get('check')
        facebook = request.POST.get('facebook')
        instagram = request.POST.get('instagram')
        twitter = request.POST.get('twitter')
        linkedin = request.POST.get('linkedin')
        pinterest = request.POST.get('pinterest')
        website = request.POST.get('website')

        '''
        We verify that users checked that comes from the frontend to validate whether the user wants to have
        their social networks for all destinations or if you want to use social networks for each destination.
        '''
        if use_default_networks == None:
            use_default_networks = False
        else:
            use_default_networks = True

        try:

            social_network = SocialNetwork.objects.get(destination__pk=request.POST.get('destination'))

            if  social_network:

                add = SocialNetwork.objects.filter(destination__user=self.request.user)
                destinos = Destination.objects.filter(user=self.request.user)
                errors = _("There is already a configuration of social networks. Do you want to update?")
                return render(request, self.template_name, {'add':add, 'destinos':destinos, 'errors': errors})
        except:
            destino = Destination.objects.get(id=request.POST.get('destination'))
            SocialNetwork.objects.create(
                destination = destino,
                social_network = use_default_networks,
                facebook =facebook,
                instagram = instagram,
                twitter = twitter,
                linkedin = linkedin,
                website = website,
                pinterest = pinterest
            )
            return HttpResponseRedirect(self.success_url)

    def delete(self,request):
        pk_social= QueryDict(request.body)
        social = get_object_or_404(SocialNetwork, pk=pk_social['pk'])
        if social.delete() :
            return JsonResponse(
                {
                'status':True
                },
                safe=False,
            )


class SocialNetworkUpdateView(UpdateView):
    template_name = 'destinations/_socialNetworkListEdit.html'
    success_url = reverse_lazy('destinations:social-network')

    def get(self, request, *args, **kwargs):
        add = SocialNetwork.objects.filter(id=kwargs['pk'])
        return render(request, self.template_name, {'social':add})


    def post(self, request, *args, **kwargs):
        #Definition of variables that return from the frontend

        use_default_networks = request.POST.get('check')
        facebook = request.POST.get('facebook')
        instagram = request.POST.get('instagram')
        twitter = request.POST.get('twitter')
        linkedin = request.POST.get('linkedin')
        website = request.POST.get('website')
        pinterest = request.POST.get('pinterest')

        '''
        We verify that users checked that comes from the frontend to validate whether the user wants to have
        their social networks for all destinations or if you want to use social networks for each destination.
        '''
        if use_default_networks == None:
            use_default_networks = False
        else:
            use_default_networks = True

        SocialNetwork.objects.filter(pk=kwargs['pk']).update(
                                                social_network = use_default_networks,
                                                facebook =facebook,
                                                instagram = instagram,
                                                twitter = twitter,
                                                linkedin = linkedin,
                                                website = website,
                                                pinterest = pinterest)

        return HttpResponseRedirect(self.success_url)


class messageView(View):
    def post(self, request, *args, **kwargs):

        subject = _('You have a new message')

        ctx = {
            'user' : request.user.email,
            'name' : request.user.get_full_name,
            'message': request.POST.get('message')
        }

        html_message = render_to_string(
            'dashboard/dashboard_email.html',
            context=ctx
        )

        message = _(f'if you want see the admin site https://travelposting.com/admin/ ')

        mail_managers(
            subject,
            message,
            fail_silently=True,
            html_message=html_message
        )

        reply = _('Thank you for your message, very soon we will answer back')

        return render(request, 'dashboard/index.html', {'reply':reply})


class MailboxView(NoCommunityRequiredMixin, View):
    template_name = 'dashboard/mailbox/_mailboxmain.html'

    def get(self, request, *args, **kwargs):
        mensajes = MessageDashboard.objects.filter(recipient=request.user).order_by('-sent_at')
        conteo = mensajes.filter(read_at=None).count()
        return render(request, self.template_name, {'mensajes':mensajes, 'conteo':conteo})

    def delete(self,request):
        pk_mail= QueryDict(request.body)
        mail = get_object_or_404(MessageDashboard, pk=pk_mail['pk'])
        if mail.delete() :
            return JsonResponse(
                {
                'status':True
                },
                safe=False,
            )


class MailboxSent(View):
    template_name = 'dashboard/mailbox/_mailboxsent.html'

    def get(self, request, *args, **kwargs):
        mensajes = MessageDashboard.objects.filter(sender=request.user).order_by('-sent_at')
        conteo = mensajes.filter(read_at=None).count()
        return render(request, self.template_name, {'mensajes':mensajes, 'conteo':conteo})


class MailboxAdd(View):
    template_name = 'dashboard/mailbox/_mailboxadd.html'
    success_url = reverse_lazy('destinations:mailbox')

    def get(self, request, *args, **kwargs):
        usuarios = CustomerUser.objects.all().exclude(email=request.user.email)
        return render(request, self.template_name, {'usuarios':usuarios})

    def post(self, request, *args, **kwargs):
        reply = _('Thank you for your message, very soon we will answer back')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        user_sender = CustomerUser.objects.get(pk=request.user.id)
        #this filter will be used when we apply all the group for magnament the other dashboard!
        admins = ['Manager']
        gr = request.user.groups.get_queryset().filter(name__in=admins).exists()
        #por el momento solo se enviara al admin los mensajes de todos los usuarios por lo que seusa
        #support@travelpostig.com
        re_admin = CustomerUser.objects.get(email='info@xposting-service.com')       
        if not gr:
            MessageDashboard.objects.create(
                subject=subject,
                content=message,
                sender=user_sender,
                recipient= re_admin
            )

            #now we send the mail
            subject = subject

            ctx = {
                'user' : request.user.email,
                'name' : request.user.get_full_name,
                'message': request.POST.get('message')
            }

            html_message = render_to_string(
                'dashboard/dashboard_email.html',
                context=ctx
            )

            message = _(f'if you want see the admin site https://travelposting.com/admin/ ')

            mail_managers(
                subject,
                message,
                fail_silently=True,
                html_message=html_message
            )
        else:
            recipient = CustomerUser.objects.get(id=request.POST.get('recipient'))
            MessageDashboard.objects.create(
                subject=subject,
                content=message,
                sender=user_sender,
                recipient= recipient
            )  

            send_mail(
                subject,
                message,
                request.user.email,
                [recipient.email],
            )          


        return HttpResponseRedirect(self.success_url)

'''
Function for reply message
'''
class MailboxReply(View):
    template_name = 'dashboard/mailbox/_mailboxReply.html'
    success_url = reverse_lazy('destinations:mailbox')

    def get(self, request, *args, **kwargs):
        pk = kwargs['int']
        mensaje = MessageDashboard.objects.get(id=pk)
        return render(request, self.template_name, {'mensaje':mensaje})

    def post(self, request, *args, **kwargs):
        reply = _('Thank you for your message, very soon we will answer back')
        message = request.POST.get('message')
        user_sender = CustomerUser.objects.get(pk=request.user.id)
        pk = kwargs['int']
        mensaje = MessageDashboard.objects.get(id=pk)
        subject = str("Rw: "+mensaje.subject) 

        MessageDashboard.objects.create(
            subject=subject,
            content=message,
            sender=user_sender,
            recipient= mensaje.sender
        )

        #now we send the mail
        subject = subject

        ctx = {
            'user' : request.user.email,
            'name' : request.user.get_full_name,
            'message': request.POST.get('message')
        }

        html_message = render_to_string(
            'dashboard/dashboard_email.html',
            context=ctx
        )

        send_mail(
            subject,
            message,
            request.user.email,
            [mensaje.sender],
        )          

        return HttpResponseRedirect(self.success_url)

'''
end function to reply message
'''
class MailboxDetail(View):
    template_name = 'dashboard/mailbox/_mailboxdetail.html'

    def get(self, request, *args, **kwargs):
        pk = kwargs['int']
        msg_pk = MessageDashboard.objects.get(pk=pk)
        if msg_pk.read_at == None:
            MessageDashboard.objects.filter(pk=pk).update(
                read_at = timezone.now()
            )

        mensajes = MessageDashboard.objects.all().order_by('-sent_at')
        conteo = mensajes.filter(read_at=None).count()
        return render(request, self.template_name, {'conteo':conteo, 'msg':msg_pk})


class LeaderView(View):
    template_name = 'dashboard/leaders/_leaders.html'

    def get(self, request, *args, **kwargs):
        admins = ['Manager']
        manager = ['manager_country']
        agencies = ['agency']
        verify_admins = request.user.groups.get_queryset().filter(name__in=admins).exists()
        if verify_admins==True:
            #search all user that group is manager_country and show their country
            users_manager_country = CustomerUser.objects.filter(groups__name='manager_country')
            users_agencies = CustomerUser.objects.filter(groups__name='agency')
            conteo = users_manager_country.count()
            conteo_agency = users_agencies.count()

            return render(request, 
                            self.template_name, 
                            {
                                'users_manager_country':users_manager_country,
                                'conteo':conteo,
                                'conteo_agency':conteo_agency,
                            }
                    )
        else:
            return render(request, self.template_name)


class LeaderAddView(CreateView):
    template_name = 'dashboard/leaders/_leaders_add.html'
    form_class = AgencyAddForm

    def form_valid(self, form):
        group, created = Group.objects.get_or_create(name='manager_country')
        form.instance.save()
        form.instance.groups.add(group)

        return super().form_valid(form)
       

class LeaderAddExistingUserView(UpdateView):
    form_class = AgencyAddExistingUserForm
    model = CustomerUser
    template_name = 'dashboard/leaders/_leaders_add_existing.html'

    def form_valid(self, form):
        group, created = Group.objects.get_or_create(name='manager_country')
        form.instance.save()
        form.instance.groups.add(group)

        return super().form_valid(form)

    def get_object(self):
        return get_object_or_404(CustomerUser, email=self.request.POST.get('email'))
                

    def get(self, request, *args, **kwargs):
        self.object = None
        context = self.get_context_data()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)


class LeaderDeleteView(DeleteView):
    model = CustomerUser
    success_url = reverse_lazy('destinations:manager')
    template_name = 'destinations/_delete.html'


class AgencyView(ListView):
    template_name = 'dashboard/leaders/_agencies.html'

    def get(self, request, *args, **kwargs):
        admins = ['Manager']
        manager = ['manager_country']
        agencies = ['agency']

        verify_admins = request.user.groups.get_queryset().filter(name__in=admins).exists()

        if verify_admins==True:
            #search all user that group is manager_country and show their country
            users_manager_country = CustomerUser.objects.filter(groups__name='manager_country')
            users_agency = CustomerUser.objects.filter(groups__name='agency')
            conteo = users_manager_country.count()
            conteo_agency = users_agency.count()

            return render(
                    request, 
                    self.template_name, 
                    {
                        'users_agency':users_agency,
                        'conteo':conteo,
                        'conteo_agency':conteo_agency,
                    })
        else:
            return render(request, self.template_name)


class AgencyUpdateView(UpdateView):
    model = CustomerUser 
    template_name = 'dashboard/leaders/_agencies_edit.html'
    form_class = AgencyEditForm


class AgencyAddView(CreateView):
    template_name = 'dashboard/leaders/_agencies_add.html'
    form_class = AgencyAddForm

    def form_valid(self, form):
        group, created = Group.objects.get_or_create(name='agency')
        form.instance.save()
        form.instance.groups.add(group)

        return super().form_valid(form)
       

class AgencyDeleteView(DeleteView):
    model = CustomerUser
    success_url = reverse_lazy('destinations:agencies')
    template_name = 'destinations/_delete.html'


class AgencyAddExistingUserView(UpdateView):
    form_class = AgencyAddExistingUserForm
    model = CustomerUser
    template_name = 'dashboard/leaders/_agencies_add_existing.html'

    def form_valid(self, form):
        group, created = Group.objects.get_or_create(name='agency')
        form.instance.save()
        form.instance.groups.add(group)

        return super().form_valid(form)

    def get_object(self):
        return get_object_or_404(CustomerUser, email=self.request.POST.get('email'))
                

    def get(self, request, *args, **kwargs):
        self.object = None
        context = self.get_context_data()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
       

class RequestDeleteView(DeleteView):
    model = Request 
    success_url = reverse_lazy('destinations:requests')
    template_name = 'dashboard/leaders/_requests_delete.html'

    def get_context_data(self, **kwargs):
        qs = self.get_queryset()
        kwargs['object_list'] = qs 
        kwargs['allow_new'] = qs.filter(status__in=[Request.PENDING, Request.APPROVED]).count() < 3
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        return Request.objects.filter(user=self.request.user)


class RequestManagerView(ListView):
    model = Request
    template_name = 'dashboard/leaders/_requests.html'
    fields = ['user', 'country', 'type']


class RequestProcessView(View):
    http_method_names = ['get']
    action = None

    def get(self, request, pk, *args, **kwargs):
        if self.action in ['approve', 'reject']:
            obj = get_object_or_404(Request, pk=pk)
            obj.status=Request.APPROVED if self.action == 'approve' else Request.REJECTED
            obj.save()
            return HttpResponseRedirect(reverse('dashboard:requests_manager'))
        else:
            raise Http404


class RequestView(UserPassesTestMixin, CreateView):
    model = Request
    template_name = 'dashboard/leaders/_requests.html'
    form_class = RequestForm
    success_url = reverse_lazy('destinations:requests')
    object = None
    login_url = reverse_lazy('destinations:requests_manager')
    raise_exception = False

    def  handle_no_permission(self):
        return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())


    def test_func(self):
        return not self.request.user.groups.filter(name__in=['manager_country', 'Manager']).exists()

    @never_cache
    def dispatch(self, *args, **kwargs):
        return super(). dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.save()
        return self.render_to_response(self.get_context_data())

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data())

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user })
        return kwargs

    def get_context_data(self, **kwargs):
        qs = self.get_queryset()
        kwargs['object_list'] = qs 
        kwargs['allow_new'] = qs.filter(status__in=[Request.PENDING, Request.APPROVED]).count() < 3
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        return Request.objects.filter(user=self.request.user)



class DocumentView(ListView):
    model = File
    template_name = 'dashboard/file/_file.html'
    fields = ['user', 'name', 'description', 'image', 'created_on', 'status']


    def delete(self,request):
        pk_document = QueryDict(request.body)
        document = get_object_or_404(File, pk=pk_document['pk'])
        if document.delete():
            return JsonResponse(
                {
                'status':True
                },
                safe=False,
            )

class DocumentAdd(CreateView):
    template_name = 'dashboard/file/_file_add.html'
    form_class = FileAddForm
    success_url = reverse_lazy('dashboard:documents')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DocumentUpdateView(UpdateView):
    template_name = 'dashboard/file/_file_update.html'
    form_class = FileAddForm
    success_url = reverse_lazy('destinations:documents')

    def get(self, request, *args, **kwargs):
        archivo = File.objects.filter(id=kwargs['pk'])
        return render(request, self.template_name, {'archivo':archivo})

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        if status == 1:
            status == True
        else: 
            status == False
            
        try:
            file_rules = request.FILES['image']
            data = File.objects.get(pk=kwargs['pk'])
            data.image = request.FILES['image']    
            data.save()
        except MultiValueDictKeyError:
            file_rules = ''


        File.objects.filter(pk=kwargs['pk']).update(
            name = name,
            description = description,
            status = status
        )

        return HttpResponseRedirect(self.success_url)

class FileDocumentsView(ListView):
    model = File
    template_name = 'dashboard/file/_file_documents.html'
    fields = ['user', 'name', 'description', 'image', 'created_on', 'status']
    queryset = File.objects.filter(status=True)


class SearchDocumentsView(ListView):
    model = File
    template_name = 'dashboard/file/_file_search.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = File.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query) | Q(image__icontains=query)
        )
        return object_list