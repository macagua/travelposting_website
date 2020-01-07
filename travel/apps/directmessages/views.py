import logging
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.accounts.models import CustomerUser
from apps.payments.paypal.views import SubscriptionView
from config.settings import local as settings
from django.core.mail import mail_managers
from django.forms.forms import BaseForm
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.shortcuts import (
    render,
    redirect,
    reverse,
)
from django.views.generic import (
    DetailView,
    UpdateView,
    View,
)
from django.views.i18n import set_language
from django.contrib.auth import authenticate, login
from django.utils.translation import gettext as _
from .models import Message
from .signals import message_read, message_sent
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.http import JsonResponse
from django.utils import timezone
from apps.destinations.models import (
    Destination,

)


class sendViews(View):
    def post(self, request, *args, **kwargs):
        subject = request.POST.get("subject")
        sender = request.POST.get("sender")
        recipient = request.POST.get("recipient")
        content = request.POST.get("message")

        sender = CustomerUser.objects.get(id=sender)
        recipient = CustomerUser.objects.get(id=recipient)

        if sender == recipient:
            raise ValidationError("You can't send messages to yourself.")

        message = Message(
                        sender=sender, 
                        recipient=recipient,
                        subject=subject,
                        content=content)
        message.save()

        message_sent.send(
            sender=message, from_user=message.sender, to=message.recipient)

        text = _("Your message has been sent successfully")

        subject = _('You have a new message')

        ctx = {
            'sender':  sender,
        }
        html_message = render_to_string(
            'community/dashboard/_email_inbox.html',
            context=ctx
        )

        message = _(
            f'if you want see the admin site https://travelposting.com/admin/ ')


        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [recipient.email],
            fail_silently=False,
            html_message=html_message
        )

        #return redirect(reverse('profile_detail', kwargs={'slug': recipient.id}))
        recipient = Message.objects.filter(recipient=request.user)
        sender = Message.objects.filter(sender=request.user)
        user = CustomerUser.objects.filter(is_community=True)

        return render(request, 'community/dashboard/mail.html', {'recipient': recipient, 'sender': sender, 'user': user, 'text':text})


class InboxView(View):
    def get(self, request, *args, **kwargs):
        recipient = Message.objects.filter(recipient=request.user)
        sender = Message.objects.filter(sender=request.user)
        user = CustomerUser.objects.filter(is_community=True)
        destino = Destination.objects.filter(
            is_deleted=False, is_published=True).order_by('?')[:3]

        return render(request, 'community/dashboard/mail.html', {'recipient':recipient, 'sender':sender, 'user':user, 'destino':destino})


class NotificationsView(View):
    def get(self, request, *args, **kwargs):
        recipient = Message.objects.filter(recipient=request.user)
        return render(request, 'community/dashboard/notifications.html', {'recipient': recipient})



def validate_message(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        message = Message.objects.get(id=post_id)

        message.read_at = timezone.now()
        message.save()
        return HttpResponse('success')
    else:
        return HttpResponse("unsuccesful")
