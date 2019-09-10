from django.urls import path

from tour.destinations import views

app_name = 'destinations'
urlpatterns = [
    path(
        '',
        views.DestinationListView.as_view(),
        name='list',
    ),

    path(
        'create/',
        views.DestinationCreateView.as_view(),
        name='create',
    ),

    path(
        '<int:pk>/create/',
        views.DestinationDetailView.as_view(),
        name='detail',
    ),

    path(
        '<int:pk>/update/',
        views.DestinationUpdateView.as_view(),
        name='update',
    ),

    path(
        '<int:pk>/delete/',
        views.DestinationDeleteView.as_view(),
        name='delete',
    ),

    path(
        '<int:pk>/gallery/',
        views.GalleryListView.as_view(),
        name='gallery-list',
    ),

    path(
        'option/<int:pk>/template/',
        views.OptionTabDataTemplateAjaxView.as_view(),
        name='option-template',
    ),
]
