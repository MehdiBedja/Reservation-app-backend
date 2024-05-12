# reservation_app/serializers.py

from rest_framework import serializers

from accounts_app.models import CustomUser
from accounts_app.serializers import UserSerializer
from parking_info_app.serializers import ParkingSerializer
from .models import ParkingPlace, Reservation

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


class ParkingPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingPlace
        fields = ['id', 'attributes']  # Include only the fields from the ParkingPlace model


class ReservationSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Assuming CustomUserSerializer is defined in accounts_app
    parking_place = ParkingPlaceSerializer()  # Assuming ParkingPlaceSerializer is defined in parking_info_app

    class Meta:
        model = Reservation
        fields = ['id', 'user', 'parking_place', 'reservation_date', 'entry_datetime', 'exit_datetime', 'payment_status', 'reservation_code']


class ReservationSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'user', 'parking_place', 'entry_datetime', 'exit_datetime', 'payment_status', 'reservation_code']