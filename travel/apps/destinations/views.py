import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.detail import BaseDetailView, SingleObjectMixin
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    ListView,
)
from oauth2_provider.views import (
    ApplicationRegistration,
    ApplicationUpdate,
    ApplicationDetail,
    ApplicationDelete,
    AuthorizedTokensListView,
    AuthorizedTokenDeleteView,
)
from tour.destinations.forms import (
    DestinationForm,
    TourDataForm,
    HeaderSectionInlineForm,
    DestinationDetailForm,
    ApplicationForm,
)
from tour.destinations.models import (
    Destination,
    TourData,
    HeaderSection,
    DestinationDetail,
    OptionTabData,
)
from tour.destinations.utils import (
    BaseInlineModelFormMixin,
    JSONResponseMixin,
    ModelEncoder,
)


logger = logging.getLogger(__name__)


class DestinationListView(LoginRequiredMixin, ListView):
    template_name = 'destinations/_list.html'
    queryset = Destination.objects.filter(is_deleted=False)

    def get_queryset(self):
        queryset = super(DestinationListView, self).get_queryset()
        return queryset.filter(user=self.request.user)


class BaseDestinationView(LoginRequiredMixin, BaseInlineModelFormMixin):
    template_name = 'destinations/_form.html'
    form_class = DestinationForm
    queryset = Destination.objects.filter(is_deleted=False)
    success_url = reverse_lazy('destinations:list')

    def get_initial(self):
        return {'user': self.request.user}

    def get_inline_tour_data_class(self):
        self.inline_tour_data_class = inlineformset_factory(
            Destination,
            TourData,
            form=TourDataForm,
            # formset=tour_dataInlineFormSet,
            extra=1,
            min_num=0,
            max_num=1,
            validate_max=True,
            validate_min=True
        )

    def get_inline_header_class(self):
        self.inline_header_class = inlineformset_factory(
            Destination,
            HeaderSection,
            form=HeaderSectionInlineForm,
            # formset=headerInlineFormSet,
            extra=1,
            min_num=0,
            max_num=1,
            validate_max=True,
            validate_min=True
        )

    def get_inline_destination_detail_class(self):
        self.inline_destination_detail_class = inlineformset_factory(
            Destination,
            DestinationDetail,
            form=DestinationDetailForm,
            # formset=destination_detailInlineFormSet,
            extra=1,
            min_num=0,
            max_num=1,
            validate_max=True,
            validate_min=True
        )

    def get_context_data(self, **kwargs):
        context = {}

        if 'tour_data_inlineformset' not in kwargs:
            self.get_inline_tour_data_class()
            context['tour_data_inlineformset'] = self.get_form_inline(
                self.inline_tour_data_class)

        if 'header_inlineformset' not in kwargs:
            self.get_inline_header_class()
            context['header_inlineformset'] = self.get_form_inline(
                self.inline_header_class)

        if 'destination_detail_inlineformset' not in kwargs:
            self.get_inline_destination_detail_class()
            context['destination_detail_inlineformset'] = self.get_form_inline(
                self.inline_destination_detail_class)
        context.update(kwargs)
        return super().get_context_data(**context)

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs.update({
    #         'error_class': LiErrorList
    #     })
    #     return kwargs

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        self.get_inline_tour_data_class()
        tour_data_inlineformset = self.get_form_inline(
            self.inline_tour_data_class)
        self.get_inline_header_class()
        header_inlineformset = self.get_form_inline(self.inline_header_class)
        self.get_inline_destination_detail_class()
        destination_detail_inlineformset = self.get_form_inline(
            self.inline_destination_detail_class)

        if form.is_valid() and tour_data_inlineformset.is_valid(
        ) and header_inlineformset.is_valid() and destination_detail_inlineformset.is_valid():
            return self.form_valid(
                form, tour_data_inlineformset, header_inlineformset,
                destination_detail_inlineformset)
        else:
            return self.form_invalid(
                form, tour_data_inlineformset, header_inlineformset,
                destination_detail_inlineformset)

    def form_valid(
            self, form, tour_data_inlineformset, header_inlineformset,
            destination_detail_inlineformset):
        self.object = form.save()

        tour_data_inlineformset.instance = self.object
        self.inline_tour_data_object = tour_data_inlineformset.save()
        header_inlineformset.instance = self.object
        self.inline_header_object = header_inlineformset.save()
        destination_detail_inlineformset.instance = self.object
        self.inline_destination_detail_object = destination_detail_inlineformset.save()

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(
            self, form, tour_data_inlineformset, header_inlineformset,
            destination_detail_inlineformset):
        # self.add_error_message(self.get_error_message())
        kwargs = {
            'form': form,
            'tour_data_inlineformset': tour_data_inlineformset,
            'header_inlineformset': header_inlineformset,
            'destination_detail_inlineformset': destination_detail_inlineformset}
        return self.render_to_response(self.get_context_data(**kwargs))


class DestinationCreateView(BaseDestinationView, CreateView):
    extra_context = {
        'submit': _('Agregar destino')
    }

    def post(self, request, *args, **kwargs):
        self.object = None
        return super(
            DestinationCreateView, self).post(
            request, *args, **kwargs)


class DestinationUpdateView(BaseDestinationView, UpdateView):
    extra_context = {
        'submit': _('Actualizar destino')
    }

    def get_form_inline_kwargs(self):
        kwargs = super().get_form_inline_kwargs()

        if hasattr(self, 'object'):
            kwargs.update({
                'instance': self.object
            })
        return kwargs

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        return super().post(request, *args, **kwargs)

    def form_valid(
            self, form, tour_data_inlineformset, header_inlineformset,
            destination_detail_inlineformset):
        self.object = form.save()

        self.inline_tour_data_object = tour_data_inlineformset.save()
        self.inline_header_object = header_inlineformset.save()
        self.inline_destination_detail_object = destination_detail_inlineformset.save()

        return HttpResponseRedirect(self.get_success_url())


class DestinationDetailView(LoginRequiredMixin, DetailView):
    template_name = 'destinations/_details.html'
    queryset = Destination.objects.filter(is_deleted=False)


class DestinationDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'destinations/_delete.html'
    queryset = Destination.objects.filter(is_deleted=False)
    success_url = reverse_lazy('destinations:list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_deleted = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class OptionTabDataTemplateAjaxView(
        LoginRequiredMixin, JSONResponseMixin, BaseDetailView):
    model = OptionTabData

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(
            context, encoder=ModelEncoder, **response_kwargs)


class GalleryListView(LoginRequiredMixin, SingleObjectMixin, ListView):
    template_name = 'destinations/gallery/_list.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Destination.objects.all())
        return super(GalleryListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GalleryListView, self).get_context_data(**kwargs)
        context['destination'] = self.object
        return context

    def get_queryset(self):
        return self.object.gallery.all()


class ApplicationCreateView(ApplicationRegistration):
    template_name = 'oauth2/application_form.html'
    form_class = ApplicationForm
    extra_context = {
        'title': _('Registrar aplicación')
    }

    def get_form_class(self):
        return self.form_class

    def get_success_url(self):
        return reverse_lazy('oauth2-application-detail',
                            kwargs={'pk': self.object.pk})


class ApplicationUpdateView(ApplicationUpdate):
    template_name = 'oauth2/application_form.html'
    form_class = ApplicationForm
    extra_context = {
        'title': _('Actualizar')
    }

    def get_form_class(self):
        return self.form_class

    def get_success_url(self):
        return reverse_lazy('oauth2-application-detail',
                            kwargs={'pk': self.object.pk})


class ApplicationDetailView(ApplicationDetail):
    template_name = 'oauth2/application_detail.html'


class ApplicationDeleteView(ApplicationDelete):
    template_name = 'oauth2/application_delete.html'
    success_url = reverse_lazy('oauth2-application-list')


class AuthorizedTokenListView(AuthorizedTokensListView):
    template_name = 'oauth2/authorized_token_list.html'


class AuthorizedTokenRevokeView(AuthorizedTokenDeleteView):
    template_name = 'oauth2/authorized_token_revoke.html'
    success_url = reverse_lazy("oauth2-authorized-token-list")