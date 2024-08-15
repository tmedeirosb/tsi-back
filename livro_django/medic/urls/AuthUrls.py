from django.urls import path
from medic.views.AuthView import login_view

urlpatterns = [
    path("login", login_view, name='login'),
]