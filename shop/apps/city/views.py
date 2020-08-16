from rest_framework import generics, status
from rest_framework.response import Response

from .models import City
from .serializers import CityListSerializer


class CityListView(generics.ListAPIView):
    """"Output a list of cities"""
    serializer_class = CityListSerializer
    queryset = City.objects.all()

