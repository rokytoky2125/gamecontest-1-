from django.urls import path
from games.views import ball

urlpatterns = [
    path("ballgame/", ball),
]