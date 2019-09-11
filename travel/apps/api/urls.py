from rest_framework.routers import DefaultRouter

from apps.api.views import DestinationViewSet
from django.urls import path, include


app_name = 'api'
router = DefaultRouter()
router.register(r'destinations', DestinationViewSet)

urlpatterns = [
    path(
        '',
        include(router.urls),
    ),
]
