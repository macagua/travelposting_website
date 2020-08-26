from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import path

from apps.accounts.models import CustomerUser
from apps.destinations.charts import (
    BookingCharts,
    DashboardIndex,
    DestinationCharts,

)
from apps.destinations.views.visitor import (
    VisitorView,
)

from apps.destinations.views.destination import (
    AgencyAddView,
    AgencyDeleteView,
    AgencyAddExistingUserView,
    AgencyUpdateView,
    AgencyView,
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
    RequestDeleteView,
    RequestManagerView,
    RequestProcessView,
    RequestView,
    SocialNetworkListView,
    SocialNetworkUpdateView,
    MailboxView,
    MailboxAdd,
    MailboxReply,
    MailboxDetail,
    MailboxSent,
    messageView,
    LeaderView,
    LeaderAddView,
    LeaderAddExistingUserView,
    LeaderDeleteView,
    DocumentView,
    DocumentAdd,
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
        lambda u: u.is_authenticated and not u.is_community,
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
        'documents',
        nocommunity_access(DocumentView.as_view()),
        name='documents',
    ),
    path('documents/add/',
        nocommunity_access(DocumentAdd.as_view()),
        name='documents-add'
    ),
    path(
        'managers',
        nocommunity_access(LeaderView.as_view()),
        name='manager',
    ),
    path(
        'managers/add/existing',
        nocommunity_access(LeaderAddExistingUserView.as_view()),
        name='manager-add-existing'
    ),
    path(
        'managers/add/',
        nocommunity_access(LeaderAddView.as_view()),
        name='manager-add',
    ),
    path(
        'managers/<int:pk>/delete',
        nocommunity_access(LeaderDeleteView.as_view()),
        name='manager-delete'
    ),
    path(
        'agencies/list',
        nocommunity_access(AgencyView.as_view()),
        name='agencies',
    ),
    path(
        'agencies/add/existing',
        nocommunity_access(AgencyAddExistingUserView.as_view()),
        name='agency-add-existing'
    ),
    path(
        'agencies/add',
        nocommunity_access(AgencyAddView.as_view()),
        name='agency-add'
    ),
    path(
        'agencies/<int:pk>/delete',
        nocommunity_access(AgencyDeleteView.as_view()),
        name='agency-delete'
    ),

    path(
        'agencies/<int:pk>/',
        nocommunity_access(AgencyUpdateView.as_view()),
        name='agency-edit'
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
        'requests/manager',
        nocommunity_access(RequestManagerView.as_view()),
        name='requests_manager',
    ),
    path(
        'requests/<int:pk>/approve/',
        nocommunity_access(RequestProcessView.as_view(action='approve')),
        name='requests_approve',
    ),

    path(
        'requests/<int:pk>/reject/',
        nocommunity_access(RequestProcessView.as_view(action='reject')),
        name='requests_reject',
    ),

    path(
        'requests/<int:pk>/delete/',
        nocommunity_access(RequestDeleteView.as_view()),
        name='requests_delete',
    ),

    path(
        'requests/',
        nocommunity_access(RequestView.as_view()),
        name='requests',
    ),

    path(
        'visitor/',
        nocommunity_access(VisitorView.as_view()),
        name='visitor',
    ),
]
