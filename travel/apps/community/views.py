from django.db.models import Q
from django.core.mail import mail_managers
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail, EmailMessage
from django.core.paginator import Paginator  # < Import the Paginator class
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import (
        get_object_or_404,
        render,
        redirect,
        reverse,
)
from django.template.loader import render_to_string
from django.template import loader
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import (
    View,
    ListView,
    UpdateView
)

from django_registration.backends.activation.views import RegistrationView

from config.settings import local as settings

from apps.accounts.models import Comment, Contact, CustomerUser
from apps.accounts.forms import CustomerUserChangeForm
from apps.community.models import Referral
from apps.destinations.models import Destination
from .forms import CommunitySignUpForm, CompleteProfileForm, SignInForm
from .models import Recommendation
from apps.utils.views import get_referal_code
from PIL import Image, ImageDraw, ImageFont
import os



def ajax_required(f):
    """
   AJAX request required decorator
   use it in your views:

   @ajax_required
   def my_view(request):
       ....

   """

    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()
        return f(request, *args, **kwargs)

    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap


def heartView(request):
    """@TODO: que es esto?"""
    pk = request.GET.get('pk', None)
    book = Book.objects.get(pk=pk)
    book.like = True
    book.save()
    data = {'book', book}
    return JsonResponse('data')


class CommmunityView(View):
    """
        Vista para pagina comunidad
    """

    def get(self, request, *args, **kwargs):
        return render(request, 'community.html')


class LoginCommunity(View):
    template_name = 'community/registration/login.html'
    form = SignInForm

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name,
            {'form': self.form},
        )

    def post(self, request, *args, **kwargs):
        user = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(
            username=user, password=password, is_community=True)

        if user is not None:
            login(request, user)
            return redirect(reverse('dashboard-community'))
        else:
            errors = _('An error, Incorrect User or Password has occurred.')

            return render(
                request,
                self.template_name,
                {'form': self.form, 'errors': errors},
            )


class signupCommunity(RegistrationView):
    email_body_template = 'accounts/mail_body.html'
    html_email_template_name = 'accounts/mail_body.html'
    email_subject_template = 'accounts/registration/activation_email_subject.txt'
    success_url = reverse_lazy('accounts:register-complete')
    template_name = 'community/registration/signup.html'
    form_class = CommunitySignUpForm

    def send_activation_email(self, user):
        code = self.get_form_kwargs()['data']['referal']
        if code:
            patrocinador = CustomerUser.objects.get(ref_code=code)
            Referral.objects.create(
                user=user,
                referredBy=patrocinador,
                code='ref',
            )
        html_email = None
        activation_key = self.get_activation_key(user)
        context = self.get_email_context(activation_key)
        context['user'] = user
        subject = loader.render_to_string(
            self.email_subject_template, context, request=self.request)
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())
        body = loader.render_to_string(self.email_body_template, context)

        if self.html_email_template_name is not None:
            html_email = loader.render_to_string(
                self.html_email_template_name, context)

        user.email_user(subject, body, settings.DEFAULT_FROM_EMAIL,
                        html_message=html_email)

        self.send_notify_managers_email(user)

    def send_notify_managers_email(self, user):
        context = {
            'user': user
        }
        subject = loader.render_to_string(
            'accounts/registration/notify_register_admin_subject.html', context)
        subject = ''.join(subject.splitlines())
        html_body = loader.render_to_string(
            'accounts/registration/notify_register_admin_body.html', context)
        mail_managers(subject, 'Nuevo usuario registrado',
                      html_message=html_body)


class ForgetPasswordCommunity(View):
    """
        Login para los usuarios de la comunidad
    """

    def get(self, request, *args, **kwargs):
        return render(request, 'community/registration/forget_password.html')


class DashboardCommunity(View):
    """
        Login para los usuarios de la comunidad
    """
    paginate_by = 3

    def get(self, request, *args, **kwargs):
        count = CustomerUser.objects.filter(is_active=True, is_community=True).count()
        # Followers
        members = Contact.objects.filter(
                Q(user_from=request.user)|Q(user_to=request.user)
                )

        paginator = Paginator(members, 6)
        page = request.GET.get('page')
        members = paginator.get_page(page)

        destination = Destination.objects.filter(
            is_deleted=False, is_published=True)

        return render(request, 'community/dashboard/dashboard.html',
                {'members': members, 'count': count, 'destination': destination})


class ProfileView(View):
    def get(self, request):
        exist_user = CustomerUser.objects \
            .filter(pk=request.user.id) \
            .filter(is_active=True) \
            .filter(is_community=True) \
            .exists()
        if exist_user:
            return render(request, 'community/profile/my_profile.html')
        else:
            return redirect('dashboard-community')


class ProfileEditView(View):
    def get(self, request):
        if request.user.is_community:
            form = CustomerUserChangeForm(instance=request.user)
            return render(request, 'community/profile/edit_profile.html', {'form': form})
        else:
            return redirect('dashboard-community')

    def post(self, request):
        form = CustomerUserChangeForm(request.POST, request.FILES,
                                      instance=CustomerUser.objects.get(pk=request.user.id))
        if form.is_valid():
            form.save()
            return redirect('my-profile')
        else:
            form = CustomerUserChangeForm(instance=CustomerUser.objects.get(pk=request.user.id))
            return render(request, 'community/profile/edit_profile.html', {'form': form})


class FollowView(View):
    def post(self, request, *args, **kwargs):
        # user_id is the variable that get the id for the user to follow
        user_id = request.POST.get('id_user')
        action = request.POST.get('follow')
        # declare user
        user = CustomerUser.objects.get(id=user_id)
        if action == 'follow':
            Contact.objects.get_or_create(
                user_from=request.user,
                user_to=user)
            return redirect(reverse('profile_detail', kwargs={'slug': user_id}))
        else:
            Contact.objects.filter(user_from=request.user,
                                   user_to=user).delete()
            return redirect(reverse('dashboard-community'))


class DetailProfileView(View):
    def get(self, request, *args, **kwargs):
        members = get_object_or_404(CustomerUser, slug=kwargs.get('slug'))
        reviews = Comment.objects.filter(user_comment=members)
        paginator = Paginator(reviews, 3)
        page = request.GET.get('page')
        reviews = paginator.get_page(page)
        return render(request, 'community/dashboard/profile_user.html', {'members': members, 'reviews': reviews})


class CommentSaveView(View):
    def post(self, request, *args, **kwargs):
        user_id = request.POST.get('user_id')
        destination_id = request.POST.get('destination_id')
        name = request.POST.get('name')
        body = request.POST.get('body')

        if destination_id == '':
            dest = None
        else:
            dest = Destination.objects.get(id=destination_id)

        user = CustomerUser.objects.get(id=user_id)

        Comment.objects.create(
            post=dest,
            user_comment=user,
            name=name,
            body=body,
        )

        subject = _('New comment add')

        ctx = {
            'post': dest,
            'user_comment': user,
            'name': name,
            'body': body,
        }

        html_message = render_to_string(
            'community/dashboard/_email.html',
            context=ctx
        )

        message = _(
            f'if you want see the admin site https://travelposting.com/admin/ ')

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

        return redirect(reverse('view_detail_destination', kwargs={'slug': destination_id}))


class CommentRwSaveView(View):
    def post(self, request, *args, **kwargs):
        user_id = request.POST.get('user_id')
        destination_id = request.POST.get('destination_id')
        name = request.POST.get('name')
        body = request.POST.get('body')

        if destination_id == '':
            dest = None
        else:
            dest = Destination.objects.get(id=destination_id)

        user = CustomerUser.objects.get(id=user_id)

        Comment.objects.create(
            post=dest,
            user_comment=user,
            name=name,
            body=body,
        )

        subject = _('New comment add')

        ctx = {
            'post': dest,
            'user_comment': user,
            'name': name,
            'body': body,
        }

        html_message = render_to_string(
            'community/dashboard/_email.html',
            context=ctx
        )

        message = _(
            f'if you want see the admin site https://travelposting.com/admin/ ')

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

        return redirect(reverse('view_detail_destination', kwargs={'slug': destination_id}))


class MakeRecomendationView(View):
    def get(self, request, *args, **kwargs):
        id_destination = Destination.objects.get(id=kwargs.get('slug'))
        return render(request, 'community/dashboard/make_recomm.html', {'id_destination': id_destination})

    def post(self, request, *args, **kwargs):

        usuario = request.POST.get('usuario')
        destino = request.POST.get('destino')
        recomendacion1 = request.POST.get('recomendacion1')
        recomendacion2 = request.POST.get('recomendacion2')

        if destino == '':
            dest = None
        else:
            dest = Destination.objects.get(id=destino)

        user = CustomerUser.objects.get(id=usuario)

        Recommendation.objects.create(
            destino=dest,
            user_recommendation=user,
            recommendation=recomendacion1,
            recommendation2=recomendacion2,
        )

        subject = _('New comment add')

        ctx = {
            'dest': dest,
            'user_recommendation': user,
            'recomendacion1': recomendacion1,
            'recomendacion2': recomendacion2,
        }

        html_message = render_to_string(
            'community/dashboard/_recommendation.html',
            context=ctx
        )

        message = _(
            f'if you want see the admin site https://travelposting.com/admin/ ')

        # mail_managers(subject,
        #              message,
        #              fail_silently=True,
        #              html_message=html_message
        #              )

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [dest.user.email],
            fail_silently=False,
            html_message=html_message
        )

        return redirect(reverse('view_detail_destination', kwargs={'slug': destino}))


class SearchResultsView(ListView):
    model = CustomerUser
    template_name = 'accounts/customeruser_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')

        object_list = CustomerUser.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(email__icontains=query) |
            Q(country__icontains=query)
        ).filter(is_community=True)

        return object_list


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            form = PasswordChangeForm(request.user)
            msg = _('Your password was successfully updated!')
            return render(request, 'accounts/change_password.html', {
                'form': form,
                'msg': msg
            })

        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })

class CompleteProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'community/profile/complete_profile.html'
    template_email = 'accounts/mail_profile_complete.html'
    model = CustomerUser
    form_class = CompleteProfileForm 
    success_url = reverse_lazy('dashboard-community')

    def get_object(self, *args, **kwargs):
        return get_object_or_404(CustomerUser, id=self.request.user.id)

    def form_valid(self, form ):
        success = super().form_valid(form)
        self.object.save()
        campaign_ref_code = settings.CAMPAIGN_REF_CODE if hasattr(settings, 'CAMPAIGN_REF_CODE') else 'TPCW-20'

        if self.request.user.user.referredBy.ref_code == campaign_ref_code and not self.request.user.ref_code.startswith('TPCW-'):

            count = Referral.objects.filter(
                    referredBy__ref_code=campaign_ref_code).exclude(user__first_name=None, user__avatar=None).count()

            if count <= settings.CAMPAIGN_COUPON_LIMIT:
                campaign_ref_code += '-'
                coupon_code = campaign_ref_code + str(count+1).zfill(len(str(settings.CAMPAIGN_COUPON_LIMIT)))
                counter = count 
                while CustomerUser.objects.filter(ref_code=coupon_code).exists():
                    counter =+ 1
                    coupon_code = campaign_ref_code + str(counter).zfill(len(str(settings.CAMPAIGN_COUPON_LIMIT)))
                self.request.user.ref_code = coupon_code
                self.request.user.save()
                
                # cover for campaign
                Image1 = Image.open('main/static/img/campaign/front.jpg') 
                # make a copy the image so that the  
                # original image does not get affected 
                Image1copy = Image1.copy() 
                #get the image from user
                Image2 = Image.open(self.request.FILES['avatar']) 
                new_image2 = Image2.resize((320, 320))
                Image2copy = new_image2.copy()
                # paste image giving dimensions 
                Image1copy.paste(Image2copy, (120, 110)) 

                # save the image  
                Image1copy.save('main/media/id_campaign/'+str(self.request.user.id)+'_front.jpg')
                
                #now we save the back file front
                Image3 = Image.open('main/static/img/campaign/back.jpg') 

                draw = ImageDraw.Draw(Image1)
                #define font for text 
                font = ImageFont.truetype('main/static/font/roboto/' + 'Roboto-Bold.ttf', size=24)
                #get ref_code fron user
                ref_code = coupon_code.split('-')[2]
                #get name and last name from user
                first_name = self.request.POST['first_name']
                last_name = self.request.POST['last_name']
                nombre = first_name+' '+last_name 
                color = (0, 0, 0)
                draw.text((240, 367), ref_code, font= font, fill = color)  
                draw.text((540, 367), nombre, font= font, fill = color)

                Image3.save('main/media/id_campaign/'+str(self.request.user.id)+'_back.jpg')

                #end campaign

                # This method is called when valid form data has been POSTed.
                # It should return an HttpResponse.
                body = render_to_string(
                    self.template_email, 
                    request=self.request
                )
                email_message = EmailMessage(
                    subject = _('Travelposting send a new import message'),
                    body = body,
                    from_email = settings.DEFAULT_FROM_EMAIL,
                    to = [self.request.user.email,]
                )
                email_message.content_subtype = 'html'
                email_message.attach_file('main/static/img/brasil.jpg')
                email_message.send()

        return success 
