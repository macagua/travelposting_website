from django import template
from apps.destinations.models import Destination, Categorie
from apps.landing_page.models import Testimony, Magazine
register = template.Library()

@register.inclusion_tag('services/destination/destinations.html', takes_context=True)
def destinations_list(context):
    list_destinations = Destination.objects.all().order_by('?')[:4]
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

@register.simple_tag()
def found_categorie(alias):
    return Destination.count_categorie(alias)

@register.inclusion_tag('services/magazine/magazine.html', takes_context=True)
def show_magazine(context):
    list_magazine = Magazine.objects.all()
    return {
        'list': list_magazine,
        'request': context.request,
    }