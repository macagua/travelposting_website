from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def total_visits(context, location,):
    return context.get('visits_counter').get(location, {'visits': 1})['visits']
