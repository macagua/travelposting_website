from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.forms import model_to_dict
from django.http import JsonResponse
from django.views.generic.edit import ModelFormMixin


class BaseInlineModelFormMixin(ModelFormMixin):
    inline_initial = []
    inline_prefix = None
    inlines = []

    def get_inline_initial(self):
        return self.inline_initial.copy()

    def get_inline_form_class(self):
        pass

    def get_inline_prefix(self):
        return self.inline_prefix

    def get_form_inline(self, inline_form_class=None):
        if inline_form_class is None:
            inline_form_class = self.get_inline_form_class()
        return inline_form_class(**self.get_form_inline_kwargs())

    def get_form_inline_kwargs(self):
        kwargs = {
            'initial': self.get_inline_initial(),
            'prefix': self.get_inline_prefix(),
            # 'error_class': LiErrorList
        }

        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        return kwargs

    # def get_context_data(self, **kwargs):
    #     context = {}
    #
    # def post(self, request, *args, **kwargs):
    #     pass
    #
    # def form_valid(self, form, inlines):
    #     pass
    #
    # def form_invalid(self, form, inlines):
    #     pass


class JSONResponseMixin:
    def render_to_json_response(self, context, **response_kwargs):
        return JsonResponse(
            self.get_data(context),
            **response_kwargs,
        )

    def get_data(self, context):
        del context['view']
        return context


class ModelEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, models.Model):
            return model_to_dict(o)
        return super(ModelEncoder, self).default(o)
