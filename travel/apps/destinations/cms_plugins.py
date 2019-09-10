from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from .models import DestinationsPlugin as DestinationsPluginModel



@plugin_pool.register_plugin
class DestinationsPlugin(CMSPluginBase):
    model = DestinationsPluginModel
    render_template = 'services/destination/all.html'
    cache = False
    def render(self, context, instance, placeholder):
        context = super(DestinationsPlugin, self).render(context, instance, placeholder)
        return context
