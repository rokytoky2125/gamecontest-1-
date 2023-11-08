from django.urls import path
from visited.views import visited

urlpatterns = [
    path("visited/", visited),
]