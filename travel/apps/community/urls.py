from django.urls import path
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import include, url

from apps.community.views import (
    CommmunityView, 
    LoginCommunity, 
    signupCommunity,
    ForgetPasswordCommunity,
    DashboardCommunity,
    FollowView,
    ProfileView,
    ProfileEditView,
    DetailProfileView,
    heartView,
    CommentSaveView,
    CommentRwSaveView,
    MakeRecomendationView,
)

from apps.directmessages.views import (
    InboxView,
)

from apps.community import views



urlpatterns = [
    path('', CommmunityView.as_view(), name='index'),
    #path(
    #    'login/',
    #    LoginCommunity.as_view(),
    #    name='login-community',
    #),
    path(
        'signup/',
        signupCommunity.as_view(),
        name='signup-community',
    ),
    path(
        'forget/',
        ForgetPasswordCommunity.as_view(),
        name='forgetpassword-community',
    ),
    path(
        'dashboard/',
        login_required(DashboardCommunity.as_view()),
        name='dashboard-community',
    ),

    path(
        'inbox/',
        login_required(InboxView.as_view()),
        name='inbox-community',
    ),

    path(
        'heart/',
        heartView,
        name='heart',
    ),

    path(
        'make-comment/',
        CommentSaveView.as_view(),
        name='make-comment',
    ),

    path(
        'make-rw/',
        CommentRwSaveView.as_view(),
        name='make-rw',
    ),

    path(
        'logout/',
        logout_then_login,
        name='logout-community',
    ),

    path(
        'users/follow/',
        login_required(FollowView.as_view()),
        name='user_follow',
    ),

    url(r'^dashboard/(?P<slug>\w+)',
        DetailProfileView.as_view(),
        name='profile_detail',
    ),

    url(r'^my-profile',
        ProfileView.as_view(),
        name='my-profile',
    ),

    url(r'^edit-profile',
            ProfileEditView.as_view(),
            name='my-profile',
    ),

    url(
        r'^make/(?P<slug>\w+)',
        MakeRecomendationView.as_view(),
        name='make-recomm',
    ),
]
