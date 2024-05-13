# parking_info_app/views.py
import os
from django.conf import settings
from rest_framework.decorators import api_view

from django.http import HttpResponse, JsonResponse
from parking_info_app.models import Parking
from parking_info_app.serializers import ParkingSerializer, ParkingSerializer2, ParkingWithIdSerializer

@api_view(['GET'])
def get_parkings(request):
    parkings = Parking.objects.all()
    serializer = ParkingSerializer(parkings, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_parkings_with_id(request):
    parkings = Parking.objects.all()
    serializer = ParkingWithIdSerializer(parkings, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_parking(request, pk):
    try:
        parking = Parking.objects.get(pk=pk)
        serializer = ParkingSerializer2(parking)
        return JsonResponse(serializer.data)
    except Parking.DoesNotExist:
        return JsonResponse({'error': 'Parking not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def image_view(request, image_name):
    image_path = os.path.join(settings.STATICFILES_DIRS[0], 'images', image_name)
    with open(image_path, 'rb') as f:
        return JsonResponse(f.read(), content_type='image/png')
    


