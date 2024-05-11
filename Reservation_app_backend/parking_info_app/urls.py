# parking_info_app/urls.py

from django.urls import path
from parking_info_app.views import get_parkings, get_parkings_with_id

urlpatterns = [
    path('getParkings/', get_parkings, name='parkings-list'),
    path('getParkingsId/', get_parkings_with_id, name='get_parkings_with_id'),


    
]
