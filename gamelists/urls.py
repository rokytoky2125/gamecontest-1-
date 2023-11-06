from django.urls import path
from gamelists.views import gamelist

urlpatterns = [
    path("gamelist/", gamelist),
]