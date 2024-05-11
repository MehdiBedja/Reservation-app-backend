# reservation_app/models.py

from django.db import models
from accounts_app.models import CustomUser
from parking_info_app.models import Parking


class ParkingPlace(models.Model):
    attributes = models.TextField()
    available = models.BooleanField(default=True)  # New field
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE, related_name='parking_places')

class Reservation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reservations')
    parking_place = models.ForeignKey(ParkingPlace, on_delete=models.CASCADE, related_name='reservations')
    reservation_date = models.DateTimeField(auto_now_add=True)
    entry_datetime = models.DateTimeField()
    exit_datetime = models.DateTimeField()
    payment_status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending')
    reservation_code = models.CharField(max_length=50, unique=True)

class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    notification_date = models.DateTimeField(auto_now_add=True)
