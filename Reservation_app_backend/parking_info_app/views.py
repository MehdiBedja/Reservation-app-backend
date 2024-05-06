# parking_info_app/views.py
import os
from django.conf import settings
from rest_framework.decorators import api_view

from django.http import HttpResponse, JsonResponse
from parking_info_app.models import Parking
from parking_info_app.serializers import ParkingSerializer

@api_view(['GET'])
def get_parkings(request):
    parkings = Parking.objects.all()
    serializer = ParkingSerializer(parkings, many=True)
    return JsonResponse(serializer.data, safe=False)


def image_view(request, image_name):
    image_path = os.path.join(settings.STATICFILES_DIRS[0], 'images', image_name)
    with open(image_path, 'rb') as f:
        return JsonResponse(f.read(), content_type='image/png')
