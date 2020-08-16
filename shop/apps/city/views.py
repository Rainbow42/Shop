from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import City
from .serializers import CityListSerializer


class CityListView(generics.ListAPIView):
    """"Output a list of cities"""
    serializer_class = CityListSerializer
    queryset = City.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = CityListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
