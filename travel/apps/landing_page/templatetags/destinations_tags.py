import os
import random
from django import template
from django.conf import settings
from apps.destinations.models import Destination, Categorie, Photo
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

@register.inclusion_tag('services/destination/tours.html', takes_context=True)
def show_tours(context):
    list_tours = Destination.objects.filter(categorie__name='Tour')
    list_pic_tours = Photo.objects.filter(destination__id__in=list_tours)

    return {
        'list_pic_tours': list_pic_tours,
        'list_tours': list_tours,
        'request': context.request,
    }

@register.simple_tag()
def background_image():
    path_to_images = str(settings.ROOT_DIR) + '/main/private/destinos/'
    ramdom_image = random.choice(os.listdir(path_to_images))
    return ('destinos/' + ramdom_image)
