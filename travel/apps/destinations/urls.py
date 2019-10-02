from django.urls import path

from apps.destinations.views import (
    DestinationListView,
    DestinationCreateView,
    DestinationDetailView,
    DestinationUpdateView,
    DestinationDeleteView,
    GalleryListView,
    OptionTabDataTemplateAjaxView,
    ItineraryListView,
)

app_name = 'destinations'
urlpatterns = [
    path(
        '',
        DestinationListView.as_view(),
        name='list',
    ),

    path(
        'create/',
        DestinationCreateView.as_view(),
        name='create',
    ),

    path(
        '<int:pk>/create/',
        DestinationDetailView.as_view(),
        name='detail',
    ),

    path(
        '<int:pk>/update/',
        DestinationUpdateView.as_view(),
        name='update',
    ),

    path(
        '<int:pk>/delete/',
        DestinationDeleteView.as_view(),
        name='delete',
    ),

    path(
        '<int:pk>/gallery/',
        GalleryListView.as_view(),
        name='gallery-list',
    ),

    path(
        'option/<int:pk>/template/',
        OptionTabDataTemplateAjaxView.as_view(),
        name='option-template',
    ),

    path(
        'itinerary/',
        ItineraryListView.as_view(),
        name='itinerary-list',
    ),
]
