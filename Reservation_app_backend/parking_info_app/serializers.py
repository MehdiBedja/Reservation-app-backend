# parking_info_app/serializers.py

from rest_framework import serializers
from parking_info_app.models import Parking, Commune

class ParkingSerializer(serializers.ModelSerializer):
    commune_name = serializers.SerializerMethodField()

    class Meta:
        model = Parking
        fields = ['name', 'description', 'commune_name', 'image']  # Exclude 'id' field

    def get_commune_name(self, obj):
        return obj.commune.name if obj.commune else None



class ParkingWithIdSerializer(serializers.ModelSerializer):
    commune_name = serializers.CharField(source='commune.name')  # Use source to access related field

    class Meta:
        model = Parking
        fields = ['id', 'name', 'description', 'commune_name', 'image']