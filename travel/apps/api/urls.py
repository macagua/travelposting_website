from oauth2_provider.views import TokenView
from rest_framework.routers import DefaultRouter

from apps.api.views import DestinationViewSet
from django.urls import path, include


app_name = 'apps.api'
router = DefaultRouter()
router.register(r'destinations', DestinationViewSet)

urlpatterns = [
    path(
        '',
        include(router.urls),
    ),

  path(
    'oauth2/token/',
    TokenView.as_view(),
    name='token',
    ),
]
