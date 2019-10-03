from django.urls import path
from apps.destinations.charts import (
    BookingCharts,
    DashboardIndex,
    DestinationCharts,
)
from apps.destinations.views import (
    DestinationListView,
    DestinationCreateView,
    DestinationDetailView,
    DestinationUpdateView,
    DestinationDeleteView,
    GalleryListView,
    OptionTabDataTemplateAjaxView,
    ItineraryListView,
    BookingListView,
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
        'itinerary/',
        ItineraryListView.as_view(),
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
]
