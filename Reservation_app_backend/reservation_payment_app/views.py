from django.shortcuts import get_object_or_404, render

# reservation_app/views.py

from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from accounts_app.models import CustomUser
from accounts_app.serializers import CustomUserSerializer
from parking_info_app.serializers import ParkingSerializer
from .serializers import ParkingPlaceSerializer, ReservationSerializer, ReservationSerializer2
from .models import ParkingPlace, Reservation

@api_view(['POST'])
def create_reservation(request):
    if request.method == 'POST':
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Reservation created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_reservations(request, user_id=None):
    user = get_object_or_404(CustomUser, pk=user_id)
    reservations = Reservation.objects.filter(user=user)
    serializer = ReservationSerializer(reservations, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def reservation_details(request, reservation_id):
    if request.method == 'GET':
        reservation = get_object_or_404(Reservation, id=reservation_id)
        serializer = ReservationSerializer(reservation)
        return JsonResponse(serializer.data)
    




@api_view(['POST'])
def create_reservation(request):
    if request.method == 'POST':
        serializer = ReservationSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Reservation created successfully."}, status=status.HTTP_201_CREATED)
        return JsonResponse({"message": "Failed to create reservation.", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
def available_parking_places(request, parking_id):
    try:
        parking_places = ParkingPlace.objects.filter(parking_id=parking_id, available=True)
        serialized_data = []
        for place in parking_places:
            serialized_place = {
                'id': place.id,
                'attributes': place.attributes,
                'parking': {
                    'id': place.parking.id,
                    'name': place.parking.name,
                    'description': place.parking.description,
                    'image': place.parking.image,
                    'commune_id': place.parking.commune_id
                }
            }
            serialized_data.append(serialized_place)
        return JsonResponse(serialized_data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)