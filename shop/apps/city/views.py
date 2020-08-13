from rest_framework.response import Response
from rest_framework.views import APIView
from .models import City
from .serializers import CityListSerializer


class CityListView(APIView):
    """"Output a list of cities"""

    def get(self, request):
        cities = City.objects.all()
        serializer = CityListSerializer(cities, many=True)
        return Response(serializer.data)
