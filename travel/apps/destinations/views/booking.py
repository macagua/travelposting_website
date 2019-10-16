import logging
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.http import QueryDict
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.detail import BaseDetailView, SingleObjectMixin
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    ListView,
    View,
)
from django.template.loader import render_to_string
from django.shortcuts import (
    render,
    get_object_or_404,
)
from django.core.mail import mail_managers
from django.core.mail import send_mail
from django.conf import settings

from apps.destinations.forms import (
    DestinationForm,
    TourDataForm,
    HeaderSectionInlineForm,
    DestinationDetailForm,
    ItineraryForm,
)
from apps.destinations.models import (
    Destination,
    TourData,
    HeaderSection,
    DestinationDetail,
    OptionTabData,
    Itinerary,
    Booking,
)
from apps.destinations.utils import (
    BaseInlineModelFormMixin,
    JSONResponseMixin,
    ModelEncoder,
)



logger = logging.getLogger(__name__)


class BookingSaveView(View):
    def post(self, request, *args, **kwargs):
        firts_name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        dni = request.POST.get('dni')
        cellphone = request.POST.get('cellphone')
        mail =  request.POST.get('mail')
        number_travel = request.POST.get('people_travel')
        name_booking = request.POST.get('destination')
        comment = request.POST.get('comment')
        destination = request.POST.get('destination_id')
        if destination=='':
            dest = None
        else:
            dest = Destination.objects.get(id=destination)

        Booking.objects.create(
            dni=dni,
            destination = dest,
            firts_name = firts_name,
            last_name = last_name,
            cellphone = cellphone,
            mail = mail,
            number_travel = number_travel,
            name_booking = name_booking,
            comment = comment
        )

        subject = _('New Booking registered')

        ctx = {
            'destination' : dest.name,
            'firts_name' : firts_name,
            'last_name' : last_name,
            'cellphone' : cellphone,
            'mail' : mail,
            'number_travel' : number_travel,
            'name_booking' : name_booking,
            'comment' : comment,
        }

        html_message = render_to_string(
            'pages/booking_email.html',
            context=ctx
        )

        message = _(f'if you want see the admin site https://travelposting.com/admin/ ')

        mail_managers(subject,
                    message,
                    fail_silently=True,
                    html_message=html_message
                )

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [dest.user.email],
            fail_silently=False,
            html_message=html_message
        )

        return render(request, 'pages/saveBooking.html')

class BookingListView(LoginRequiredMixin, ListView):
    template_name = 'destinations/_booking_list.html'
    queryset = Booking.objects.all()

    def get_queryset(self):
        queryset = super(BookingListView, self).get_queryset()
        return queryset.filter(destination__user=self.request.user)


class BookingSaveStat(View):
    def post(self,request):
        import ipdb; ipdb.set_trace()
        if form_map.is_valid():
            if form_map.save() :
                return JsonResponse({'msg':_('a new map has been added to your destination'),'status':True},
                    safe=False,
                )
        else:
            return JsonResponse(
                {
                'error':mapped_errors_form(form_map),
                'status':False
                },
                safe=False,
            )

class UpdateBooking(View):
    def post(self, request, *args, **kwargs):
        import ipdb; ipdb.set_trace()
        Booking.objects.filter(pk=request.POST.get('id')).update(process_status=True)
        return HttpResponseRedirect('/destinations/booking-list/')