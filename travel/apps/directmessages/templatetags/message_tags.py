import os
import random
from django import template
from django.conf import settings
from apps.directmessages.models import Message

register = template.Library()


@register.inclusion_tag('menu/notifications.html', takes_context=True)
def notifications_message(context):
    user = context.request.user
    n = Message.objects.filter(recipient=user, read_at=None)
    return {
        'notifications': n,
        'request': context.request,
    }


@register.inclusion_tag('menu/notifications_lat.html', takes_context=True)
def notifications_lat(context):
    user = context.request.user
    n = Message.objects.filter(recipient=user, read_at=None)
    return {
        'notifications': n,
        'request': context.request,
    }


@register.inclusion_tag('menu/notifications_inbox.html', takes_context=True)
def notifications_inbox(context):
    user = context.request.user
    n = Message.objects.filter(recipient=user, read_at=None)
    return {
        'notifications': n,
        'request': context.request,
    }
