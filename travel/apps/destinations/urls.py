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
    SocialNetworkListView,
    SocialNetworkUpdateView,
    messageView,
)

from apps.destinations.views.booking import (
    BookingListView,
    BookingSaveView,
    BookingSaveStat,
    UpdateBooking
)

from apps.destinations.views.maps import (
    DestinationMapView,
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
        'social-network/',
        SocialNetworkListView.as_view(),
        name='social-network',
    ),
    path(
        'social-network/delete-setting',
        SocialNetworkListView.as_view(),
        name='delete-setting',
    ),
    path(
        '<int:pk>/up/',
        SocialNetworkUpdateView.as_view(),
        name='update-social',
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
        'booking-save/',
        BookingSaveStat.as_view(),
        name='booking-save',
    ),

    path(
        'update-booking/',
        UpdateBooking.as_view(),
        name='update-booking',
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
        'maps/add-map',
        DestinationMapView.as_view(),
        name='add-map',
    ),
    path(
        'maps/update-map',
        DestinationMapView.as_view(),
        name='update-map',
    ),
    path(
        'maps/delete-map',
        DestinationMapView.as_view(),
        name='delete-map',
    ),


    path(
            'maps/',
            DestinationMapView.as_view(),
            name='destination-map',
    ),

    path(
        'message/',
        messageView.as_view(),
        name='send_message',
    ),
]
