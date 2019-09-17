from django.shortcuts import render
from django.views import View
# Create your views here.

class CommmunityView(View):
    """
        Vista para pagina comunidad
    """

    def get(self, request, *args, **kwargs):        
        return render(request, 'community.html')