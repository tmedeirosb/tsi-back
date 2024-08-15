from django.urls import path
from medic.views.HomeView import home_view
from medic.views.ListProfile import list_view

urlpatterns = [
    path("", home_view),
    path("list/", list_view),
]