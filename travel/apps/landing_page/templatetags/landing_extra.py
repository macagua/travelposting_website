import re

from django import template
from django.template.defaultfilters import stringfilter

from apps.landing_page.models import Feature

register = template.Library()


@register.filter
def show_features(plan):
    features = Feature.objects.filter(planfeature__plan=plan, planfeature__active=True).order_by('planfeature__order')
    return features


@register.filter
@stringfilter
def price(string):
    if '€' in string:
        pass


@register.filter
@stringfilter
def prefix_counter(string):
    srch = re.search(r'^\D+', string)

    if srch:
        return srch.group()
    return ''


@register.filter
@stringfilter
def number_counter(string):
    return re.sub(r'\D+', '', string)


@register.filter
def get_children_plan(feature, plan):
    return feature.get_children_active().validate_plan(plan)


@register.filter
def list_count(number):
    return range(number)
