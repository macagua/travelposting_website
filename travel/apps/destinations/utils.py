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


TEMPLATE_DESCRIPTION = """
<strong>Ingrese su título aquí...</strong><br><br>

<p> <b>Ingrese aquí su texto...</b></p>

<!--more--><br><br>

<p> <b>Ingrese más información aquí...</b></p>

<!--more--><br><br>

<strong>Quienes somos</strong><br><br>

<p><b>Por favor ingrese aquí su texto...</b></p><br><br>

<strong>Misión</strong><br><br>

<p><b>Por favor ingrese aquí su texto...</b></p><br><br>

<table class="table table-bordered tours-tabs__table" style="width: 100%px;">
<tbody>
<tr>
 <td style="width: 213px;"><strong>SALIDA / RETORNO</strong></td>
 <td style="width: 574.233px;"><b>Ingrese aquí la salida...</b></td>
</tr>
<tr>
 <td style="width: 213px;"><strong>HORA DE SALIDA</strong></td>
 <td style="width: 574.233px;"><b>Ingrese aquí la hora de salida...</b></td>
</tr>
<tr>
 <td style="width: 213px;"><strong>HORA DE LLEGADA</strong></td>
 <td style="width: 574.233px;"><b>Ingrese aquí la hora de llegada...</b></td>
</tr>
<tr>
 <td style="width: 213px;"><strong>NR. DE TOUR PARA RESERVAS</strong></td>
 <td style="width: 574.233px;"><b>Ingrese aquí el nro de tour...</b></td>
</tr>
<tr>
 <td style="width: 213px;"><strong>TRASLADO DESDE </strong></td>
 <td style="width: 574.233px;"><strong><b>Ingrese aquí el traslado...</b></strong></td>
</tr>
<tr>
 <td style="width: 213px;"><strong>INCLUIDO</strong></td>
 <td style="width: 574.233px;">
  <b>Ingrese aquí lo que va incluido en el paquete como una lista...</b>
  <ul><li><b><br></b></li><li><b><br></b></li><li><b><br></b></li></ul>
 </td>
</tr>
<tr>
 <td style="width: 213px;"><strong>NO INCLUIDO</strong></td>
 <td style="width: 574.233px;">
  <b>Ingrese aquí lo que no va incluido en el paquete como una lista...</b>
  <ul><li><b><br></b></li><li><b><br></b></li><li><b><br></b></li></ul>
 </td>
</tr>
</tbody>
</table>
"""
