from django import template
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from apps.destinations.models import Destination, Badge
register = template.Library()

@register.inclusion_tag('services/destination/destinations.html', takes_context=True)
def destinations_list(context):
    list_destinations = Destination.objects.all()[:4]
    return {
        'list': list_destinations,
        'request': context.request,
    }

@register.inclusion_tag('services/destination/categories.html', takes_context=True)
def categories_list(context):
    list_categories = Badge.objects.all()
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