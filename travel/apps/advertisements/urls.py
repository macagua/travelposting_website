from django.urls import path

from apps.advertisements.views import (
    AdvertisersListView,
    AdvertiserCreateView,
    AdvertiserUpdateView,
    AdvertiserDeleteView,
    CategoriesListView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
    AdsListView,
    AdCreateView,
    # AdDetailView,
    AdUpdateView,
    AdDeleteView,
    AdImagesListView,
    AdImageCreateView,
    AdImageUpdateView,
    AdImageDeleteView
)
from apps.destinations.urls import nocommunity_access


app_name = 'advertisements'

urlpatterns = [
    path(
        'advertiser/list/',
        nocommunity_access(AdvertisersListView.as_view()),
        name='advertisers-list',
    ),

    path(
        'advertiser/create/',
        nocommunity_access(AdvertiserCreateView.as_view()),
        name='advertiser-create',
    ),

    path(
        'advertiser/<int:pk>/update/',
        nocommunity_access(AdvertiserUpdateView.as_view()),
        name='advertiser-update',
    ),

    path(
        'advertiser/<int:pk>/delete/',
        nocommunity_access(AdvertiserDeleteView.as_view()),
        name='advertiser-delete',
    ),

    path(
        'category/list/',
        nocommunity_access(CategoriesListView.as_view()),
        name='categories-list',
    ),

    path(
        'category/create/',
        nocommunity_access(CategoryCreateView.as_view()),
        name='category-create',
    ),

    path(
        'category/<int:pk>/update/',
        nocommunity_access(CategoryUpdateView.as_view()),
        name='category-update',
    ),

    path(
        'category/<int:pk>/delete/',
        nocommunity_access(CategoryDeleteView.as_view()),
        name='category-delete',
    ),

    path(
        'ad/list/',
        nocommunity_access(AdsListView.as_view()),
        name='ads-list',
    ),

    path(
        'ad/create/',
        nocommunity_access(AdCreateView.as_view()),
        name='ad-create',
    ),

    # path(
    #     'ad/<int:pk>/',
    #     nocommunity_access(AdDetailView.as_view()),
    #     name='ad-detail',
    # ),

    path(
        'ad/<int:pk>/update/',
        nocommunity_access(AdUpdateView.as_view()),
        name='ad-update',
    ),

    path(
        'ad/<int:pk>/delete/',
        nocommunity_access(AdDeleteView.as_view()),
        name='ad-delete',
    ),

    path(
        'ad-image/list/',
        nocommunity_access(AdImagesListView.as_view()),
        name='ad-images-list',
    ),

    path(
        'ad-image/create/',
        nocommunity_access(AdImageCreateView.as_view()),
        name='ad-image-create',
    ),

    path(
        'ad-image/<int:pk>/update/',
        nocommunity_access(AdImageUpdateView.as_view()),
        name='ad-image-update',
    ),

    path(
        'ad-image/<int:pk>/delete/',
        nocommunity_access(AdImageDeleteView.as_view()),
        name='ad-image-delete',
    ),
]
