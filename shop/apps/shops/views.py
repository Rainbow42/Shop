from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Shop
from apps.street.models import Street
from .serializers import ShopCreateSerializer, ShopListSerializer
from .service import ShopFilter
from rest_framework import generics
from django.utils import timezone


class ShopListView(generics.ListAPIView):
    """Output a list of shops"""
    queryset = Shop.objects.all()
    serializer_class = ShopListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ShopFilter

    def get_queryset(self):
        queryset = Shop.objects.all()
        now = timezone.now()
        open = self.request.query_params.get('open', None)
        if open == '1':
            queryset = queryset.filter(time_close__gte=now, time_open__lte=now)
        elif open == '0':
            queryset = queryset.filter(time_close__lte=now, time_open__lte=now)
        return queryset


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
