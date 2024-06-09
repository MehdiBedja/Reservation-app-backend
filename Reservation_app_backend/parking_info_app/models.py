# parking_app/models.py

from django.db import models

class Wilaya(models.Model):
    name = models.CharField(max_length=100)

class Daira(models.Model):
    name = models.CharField(max_length=100)
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE, related_name='dairas')

class Commune(models.Model):
    name = models.CharField(max_length=100)
    daira = models.ForeignKey(Daira, on_delete=models.CASCADE, related_name='communes')

class Parking(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.CharField(max_length=255, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    commune = models.ForeignKey(Commune, on_delete=models.CASCADE, related_name='parkings')
