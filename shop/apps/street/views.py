from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Street
from .serializers import StreetDetailCitySerializer


class StreetDetailCityView(APIView):
    """"Output a all streets in the city"""

    def get(self, request, pk):
        street = Street.objects.filter(city=pk)
        serializer = StreetDetailCitySerializer(street, many=True)
        return Response(serializer.data)
