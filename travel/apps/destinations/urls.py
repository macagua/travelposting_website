from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.destinations.charts import (
    BookingCharts,
    DashboardIndex,
    DestinationCharts,

)
from apps.destinations.views.visitor import (
    VisitorView,
)

from apps.destinations.views.destination import (
    DestinationListView,
    DestinationCreateView,
    DestinationDetailView,
    DestinationUpdateView,
    DestinationDeleteView,
    GalleryListView,
    OptionTabDataTemplateAjaxView,
    ItineraryCreateView,
    ItineraryUpdateView,
    ItineraryView,
    SocialNetworkListView,
    SocialNetworkUpdateView,
    MailboxView,
    MailboxAdd,
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
        login_required(DashboardIndex),
        name='dashboard-index',
    ),

    path(
        'mailbox',
        login_required(MailboxView.as_view()),
        name='mailbox',
    ),
    path(
        'mailbox/add',
        login_required(MailboxAdd.as_view()),
        name='mailbox-add',
    ),

    path(
        'list',
        login_required(DestinationListView.as_view()),
        name='list',
    ),

    path(
        'create/',
        login_required(DestinationCreateView.as_view()),
        name='create',
    ),

    path(
        '<int:pk>/create/',
        login_required(DestinationDetailView.as_view()),
        name='detail',
    ),

    path(
        '<int:pk>/update/',
        login_required(DestinationUpdateView.as_view()),
        name='update',
    ),

    path(
        '<int:pk>/delete/',
        login_required(DestinationDeleteView.as_view()),
        name='delete',
    ),

    path(
        'social-network/',
        login_required(SocialNetworkListView.as_view()),
        name='social-network',
    ),
    path(
        'social-network/delete-setting',
        login_required(SocialNetworkListView.as_view()),
        name='delete-setting',
    ),
    path(
        '<int:pk>/up/',
        login_required(SocialNetworkUpdateView.as_view()),
        name='update-social',
    ),

    path(
        '<int:pk>/gallery/',
        login_required(GalleryListView.as_view()),
        name='gallery-list',
    ),

    path(
        'option/<int:pk>/template/',
        login_required(OptionTabDataTemplateAjaxView.as_view()),
        name='option-template',
    ),

    path(
        'itinerary/get-itinerary',
        login_required(ItineraryView.as_view()),
        name='get-itinerary',
    ),

    path(
        'itinerary/add-itinerary',
        login_required(ItineraryView.as_view()),
        name='add-itinerary',
    ),
    path(
        'itinerary/update-itinerary',
        login_required(ItineraryView.as_view()),
        name='update-itinerary',
    ),
    path(
        'itinerary/delete-itinerary',
        login_required(ItineraryView.as_view()),
        name='delete-itinerary',
    ),
    path(
        'itinerary/create/',
        login_required(ItineraryCreateView.as_view()),
        name='itinerary-create',
    ),
    path(
        'itinerary/<pk>/edit/',
        login_required(ItineraryUpdateView.as_view()),
        name='itinerary-edit',
    ),

    path(
        'itinerary/',
        login_required(ItineraryView.as_view()),
        name='itinerary-list',
    ),

    path(
        'booking-list/',
        login_required(BookingListView.as_view()),
        name='booking-list',
    ),

    path(
        'booking-charts/',
        login_required(BookingCharts),
        name='booking-charts',
    ),

    path(
        'booking-save/',
        login_required(BookingSaveStat.as_view()),
        name='booking-save',
    ),

    path(
        'update-booking/',
        login_required(UpdateBooking.as_view()),
        name='update-booking',
    ),

    path(
        'destination-charts/',
        login_required(DestinationCharts),
        name='destination-charts',
    ),

    path(
        'maps/get-list',
        login_required(MapListView.as_view()),
        name='list-maps',
    ),

    path(
        'maps/add-map',
        login_required(DestinationMapView.as_view()),
        name='add-map',
    ),
    path(
        'maps/update-map',
        login_required(DestinationMapView.as_view()),
        name='update-map',
    ),
    path(
        'maps/delete-map',
        login_required(DestinationMapView.as_view()),
        name='delete-map',
    ),


    path(
        'maps/',
        login_required(DestinationMapView.as_view()),
        name='destination-map',
    ),

    path(
        'message/',
        login_required(messageView.as_view()),
        name='send_message',
    ),

    path(
        'visitor/',
        login_required(VisitorView.as_view()),
        name='visitor',
    ),
]
