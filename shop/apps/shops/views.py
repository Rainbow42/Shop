from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Shop
from .serializers import ShopCreateSerializer


class ShopListView(APIView):
    """Сreating a shop"""

    def post(self, request):
        shop = ShopCreateSerializer(data=request.data)
        if shop.is_valid():
            shop.save()
            return Response(shop.data,  status=status.HTTP_201_CREATED)
        return Response(shop.data, status=status.HTTP_400_BAD_REQUEST)
