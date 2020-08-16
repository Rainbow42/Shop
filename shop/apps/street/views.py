from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Street
from .serializers import StreetDetailCitySerializer


class StreetDetailCityView(APIView):
    """"Output a all streets in the city"""

    def get(self, request, pk):
        street = Street.objects.filter(city=pk)
        print(street)
        serializer = StreetDetailCitySerializer(street, many=True)
        if len(street) != 0:
            return Response(serializer.data, status=200)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
