from django.urls import path

from apps.destinations import views

app_name = 'destinations'
urlpatterns = [
    path('test/', views.isuccess),

]
