from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import path

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
    MailboxReply,
    MailboxDetail,
    MailboxSent,
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


def nocommunity_access(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    nocom_decorator = user_passes_test(
        lambda u: not u.is_community,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function) and  nocom_decorator(function)
    return actual_decorator and nocom_decorator



app_name = 'destinations'
urlpatterns = [
    path(
        '',
        nocommunity_access(DashboardIndex),
        name='dashboard-index',
    ),

    path(
        'mailbox',
        nocommunity_access(MailboxView.as_view()),
        name='mailbox',
    ),
    path(
        'mailbox/sent',
        nocommunity_access(MailboxSent.as_view()),
        name='mailbox-sent',
    ),
    path(
        'mailbox/delete-mail',
        nocommunity_access(MailboxView.as_view()),
        name='delete-mail',
    ),
    path(
        'mailbox/add',
        nocommunity_access(MailboxAdd.as_view()),
        name='mailbox-add',
    ),
    path(
        'mailbox/reply/<int>',
        nocommunity_access(MailboxReply.as_view()),
        name='mailbox-reply',
    ),
    path(
        'mailbox/<int>',
        nocommunity_access(MailboxDetail.as_view()),
        name='mailbox-detail'
    ),

    path(
        'list',
        nocommunity_access(DestinationListView.as_view()),
        name='list',
    ),

    path(
        'create/',
        nocommunity_access(DestinationCreateView.as_view()),
        name='create',
    ),

    path(
        '<int:pk>/create/',
        nocommunity_access(DestinationDetailView.as_view()),
        name='detail',
    ),

    path(
        '<int:pk>/update/',
        nocommunity_access(DestinationUpdateView.as_view()),
        name='update',
    ),

    path(
        '<int:pk>/delete/',
        nocommunity_access(DestinationDeleteView.as_view()),
        name='delete',
    ),

    path(
        'social-network/',
        nocommunity_access(SocialNetworkListView.as_view()),
        name='social-network',
    ),
    path(
        'social-network/delete-setting',
        nocommunity_access(SocialNetworkListView.as_view()),
        name='delete-setting',
    ),
    path(
        '<int:pk>/up/',
        nocommunity_access(SocialNetworkUpdateView.as_view()),
        name='update-social',
    ),

    path(
        '<int:pk>/gallery/',
        nocommunity_access(GalleryListView.as_view()),
        name='gallery-list',
    ),

    path(
        'option/<int:pk>/template/',
        nocommunity_access(OptionTabDataTemplateAjaxView.as_view()),
        name='option-template',
    ),

    path(
        'itinerary/get-itinerary',
        nocommunity_access(ItineraryView.as_view()),
        name='get-itinerary',
    ),

    path(
        'itinerary/add-itinerary',
        nocommunity_access(ItineraryView.as_view()),
        name='add-itinerary',
    ),
    path(
        'itinerary/update-itinerary',
        nocommunity_access(ItineraryView.as_view()),
        name='update-itinerary',
    ),
    path(
        'itinerary/delete-itinerary',
        nocommunity_access(ItineraryView.as_view()),
        name='delete-itinerary',
    ),
    path(
        'itinerary/create/',
        nocommunity_access(ItineraryCreateView.as_view()),
        name='itinerary-create',
    ),
    path(
        'itinerary/<pk>/edit/',
        nocommunity_access(ItineraryUpdateView.as_view()),
        name='itinerary-edit',
    ),

    path(
        'itinerary/',
        nocommunity_access(ItineraryView.as_view()),
        name='itinerary-list',
    ),

    path(
        'booking-list/',
        nocommunity_access(BookingListView.as_view()),
        name='booking-list',
    ),

    path(
        'booking-charts/',
        nocommunity_access(BookingCharts),
        name='booking-charts',
    ),

    path(
        'booking-save/',
        nocommunity_access(BookingSaveStat.as_view()),
        name='booking-save',
    ),

    path(
        'update-booking/',
        nocommunity_access(UpdateBooking.as_view()),
        name='update-booking',
    ),

    path(
        'destination-charts/',
        nocommunity_access(DestinationCharts),
        name='destination-charts',
    ),

    path(
        'maps/get-list',
        nocommunity_access(MapListView.as_view()),
        name='list-maps',
    ),

    path(
        'maps/add-map',
        nocommunity_access(DestinationMapView.as_view()),
        name='add-map',
    ),
    path(
        'maps/update-map',
        nocommunity_access(DestinationMapView.as_view()),
        name='update-map',
    ),
    path(
        'maps/delete-map',
        nocommunity_access(DestinationMapView.as_view()),
        name='delete-map',
    ),


    path(
        'maps/',
        nocommunity_access(DestinationMapView.as_view()),
        name='destination-map',
    ),

    path(
        'message/',
        nocommunity_access(messageView.as_view()),
        name='send_message',
    ),

    path(
        'visitor/',
        nocommunity_access(VisitorView.as_view()),
        name='visitor',
    ),
]
