from django.urls import path
from apps.destinations.charts import (
    BookingCharts,
    DashboardIndex,
    DestinationCharts,
)
from apps.destinations.views.destination import (
    DestinationListView,
    DestinationCreateView,
    DestinationDetailView,
    DestinationUpdateView,
    DestinationDeleteView,
    GalleryListView,
    OptionTabDataTemplateAjaxView,
    ItineraryView,
)

from apps.destinations.views.booking import (
    BookingListView,
    BookingSaveView,
)

from apps.destinations.views.maps import (
    DestinationMap,
    MapListView,
)

app_name = 'destinations'
urlpatterns = [
    path(
        '',
        DashboardIndex,
        name='dashboard-index',
    ),

    path(
        'list',
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
        'itinerary/get-itinerary',
        ItineraryView.as_view(),
        name='get-itinerary',
    ),

    path(
        'itinerary/add-itinerary',
        ItineraryView.as_view(),
        name='add-itinerary',
    ),
    path(
        'itinerary/update-itinerary',
        ItineraryView.as_view(),
        name='update-itinerary',
    ),
    path(
            'itinerary/delete-itinerary',
            ItineraryView.as_view(),
            name='delete-itinerary',
    ),

    path(
        'itinerary/',
        ItineraryView.as_view(),
        name='itinerary-list',
    ),

    path(
        'booking-list/',
        BookingListView.as_view(),
        name='booking-list',
    ),

    path(
        'booking-charts/',
        BookingCharts,
        name='booking-charts',
    ),

    path(
        'destination-charts/',
        DestinationCharts,
        name='destination-charts',
    ),

    path(
            'maps/get-list',
            MapListView.as_view(),
            name='list-maps',
    ),

    path(
            'maps/',
            DestinationMap.as_view(),
            name='destination-map',
    ),
]
