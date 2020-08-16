from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Shop
from apps.street.models import Street
from .serializers import ShopCreateSerializer, ShopListSerializer


class ShopListView(APIView):
    """Output a list of shops"""

    def get(self, request):
        cities = Shop.objects.all()
        serializer = ShopListSerializer(cities, many=True)
        return Response(serializer.data, status=200)


class ShopCreateView(APIView):
    """Сreating a shop"""

    def post(self, request):
        shop = ShopCreateSerializer(data=request.data)
        data = request.data
        street = Street.objects.get(pk=data['street'])
        if street.city.id == data['city']:
            if shop.is_valid():
                shop.save()
                return Response(shop.data, status=202)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)