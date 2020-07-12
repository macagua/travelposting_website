from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.forms import model_to_dict
from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _
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


TEMPLATE_DESCRIPTION = _("""
<strong>Enter your title here...</strong><br><br>

<p> <b>Enter your text here...</b></p>

<!--more--><br><br>

<p> <b>Enter more information here...</b></p>

<!--more--><br><br>

<strong>Who we are</strong><br><br>

<p><b>Please enter your text here...</b></p><br><br>

<strong>Mission</strong><br><br>

<p><b>Please enter your text here...</b></p><br><br>

<table class="table table-bordered tours-tabs__table" style="width: 100%px;">
<tbody>
<tr>
 <td style="width: 213px;"><strong>EXIT / RETURN</strong></td>
 <td style="width: 574.233px;"><b>Enter the exit here...</b></td>
</tr>
<tr>
 <td style="width: 213px;"><strong>EXIT TIME</strong></td>
 <td style="width: 574.233px;"><b>Enter the time of exit here...</b></td>
</tr>
<tr>
 <td style="width: 213px;"><strong>ARRIVAL TIME</strong></td>
 <td style="width: 574.233px;"><b>Enter the time of arrival here...</b></td>
</tr>
<tr>
 <td style="width: 213px;"><strong>NR. OF TOUR FOR RESERVATIONS</strong></td>
 <td style="width: 574.233px;"><b>Enter the tour number here...</b></td>
</tr>
<tr>
 <td style="width: 213px;"><strong>TRANSFER FROM </strong></td>
 <td style="width: 574.233px;"><strong><b>Enter the transfer here...</b></strong></td>
</tr>
<tr>
 <td style="width: 213px;"><strong>INCLUDED</strong></td>
 <td style="width: 574.233px;">
  <b>Enter here what is included in the package as a list...</b>
  <ul><li><b><br></b></li><li><b><br></b></li><li><b><br></b></li></ul>
 </td>
</tr>
<tr>
 <td style="width: 213px;"><strong>NOT INCLUDED</strong></td>
 <td style="width: 574.233px;">
  <b>Enter here what is not included in the package as a list...</b>
  <ul><li><b><br></b></li><li><b><br></b></li><li><b><br></b></li></ul>
 </td>
</tr>
</tbody>
</table>
""")


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
