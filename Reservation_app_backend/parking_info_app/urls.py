# parking_info_app/urls.py

from django.urls import path
from parking_info_app.views import get_parkings

urlpatterns = [
    path('getParkings/', get_parkings, name='parkings-list'),
]
