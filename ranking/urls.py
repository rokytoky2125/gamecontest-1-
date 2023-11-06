from django.urls import path
from ranking.views import rank

urlpatterns = [
    path("rank/", rank),
]