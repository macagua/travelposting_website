import os
import random
from django import template
from django.conf import settings
from apps.accounts.models import CustomerUser
from apps.landing_page.models import (
    Testimony,
    Magazine,
    Plan,
    Slider,
)

from apps.destinations.models import (
    Destination,
    Categorie,
    Photo,
    GeneralDetail,
    Booking,
    MessageDashboard
)
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('services/destination/destinations.html', takes_context=True)
def destinations_list(context):
    rendered_list = []
    list_destination = Destination.objects.filter(is_deleted=False, is_published=True).order_by('?')
    for destination in list_destination:
        if destination.first_pic != None:
            rendered_list.append(destination)
            if len(rendered_list) == 4:
                break

    list_destinations = rendered_list
    return {
        'list': list_destinations,
        'request': context.request,
    }


@register.inclusion_tag('services/destination/categories.html', takes_context=True)
def categories_list(context):
    list_categories = Categorie.objects.filter(status=True)
    return {
        'list': list_categories,
        'request': context.request,
    }


@register.simple_tag()
def img_class(did):
    div ={
        1:"col-5 align-self-end",
        2:"col-7",
        3:"col-5 offset-1",
        4:"col-5"
    }
    return div[did]


@register.inclusion_tag('services/destination/testimonials.html', takes_context=True)
def testimonials_list(context):
    list_testimonials = Testimony.objects.all()
    return {
        'list': list_testimonials,
        'request': context.request,
    }


@register.inclusion_tag('services/destination/sponsors.html', takes_context=True)
def sponsors_list(context):
    list_sponsors = Slider.objects.filter(active=True)
    return {
        'list': list_sponsors,
        'request': context.request,
    }


@register.simple_tag()
def found_categorie(alias):
    return Destination.count_categorie(alias)

@register.simple_tag()
def simple_list_categorie():
    return Categorie.objects.filter(status=True)


@register.inclusion_tag('services/magazine/magazine.html', takes_context=True)
def show_magazine(context):
    list_magazine = Magazine.objects.all()
    return {
        'list': list_magazine,
        'request': context.request,
    }


@register.inclusion_tag('services/destination/tours.html', takes_context=True)
def show_tours(context):
    list_tours = Destination.objects.filter(categorie__name='Tour')
    return {
        'list_tours': list_tours,
        'request': context.request,
    }


@register.simple_tag()
def filter_photo_tours(id_tour):
    """
        SimpleTag to filter the ```Photo``` objects.

        Args:
            id_tour: id ```photo_id```to filter the queryset.

        Returns:
            A list of ```Photo```` objects filtered by requested id
    """
    list_pic_tours = Photo.objects.filter(destination=id_tour).order_by('?').first()
    return list_pic_tours


@register.simple_tag()
def filter_destination_price(id_tour):
    """
        SimpleTag to filter the ```GenetalDetail``` to get the price to getting tour.

        Args:
            id_tour: ```id``` to filter the queryset.

        Returns:
            A string  formated  with the current price of given tour.
    """
    tour_general_detail = GeneralDetail.objects.filter(destination_detail=id_tour.pk).first()
    current_destination_price = tour_general_detail.regular_price
    return current_destination_price


@register.simple_tag()
def background_image():
    path_to_images = str(settings.ROOT_DIR) + '/main/private/destinos/'
    ramdom_image = random.choice(os.listdir(path_to_images))
    return ('destinos/' + ramdom_image)


@register.inclusion_tag('services/pricing/plans.html', takes_context=True)
def show_pricing(context):
    list_pricing = Plan.objects.filter(active=True)
    return {
        'plans': list_pricing,
        'request': context.request,
    }


@register.simple_tag()
def filter_dashboard_index(user):
    """
        filter destinations and booing for dashboard.

        Args:
            user: ```id``` to filter the queryset.

        Returns:
            A string  formated  with the required request.
    """
    destination_user = Destination.objects.filter(user=user).count()
    booking_user = Booking.objects.filter(destination__user=user).count()
    user_last = CustomerUser.objects.filter(last_login__startswith=timezone.now().date()).count()

    dashboard_list = {
        'destination_count': destination_user,
        'booking_count': booking_user,
        'user_last': user_last,
    }

    return dashboard_list

@register.filter
def parse_to_list(value_int):
    list = []
    for i in range(0,value_int):
        list.append(i)
    return list


@register.inclusion_tag('dashboard/mailbox/message_accounts.html', takes_context=True)
def show_notification(context):
    mensajes = MessageDashboard.objects.filter(recipient=context.request.user, read_at=None).order_by('-sent_at')
    conteo = mensajes.filter(recipient=context.request.user, read_at=None).count()    
    return {
        'mensajes': mensajes,
        'conteo': conteo,
    }
