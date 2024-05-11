# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('myReservations/<int:user_id>/', views.get_reservations, name='get_reservations'),
    path('addReservation/', views.create_reservation, name='create_reservation'),
    path('addReservation/', views.create_reservation, name='create_reservation'),
    path('getAllParkingPlaces/<int:parking_id>/', views.available_parking_places, name='available_parking_places'),


]
