from rest_framework import serializers
from .models import Shop


class ShopCreateSerializer(serializers.ModelSerializer):
    """Сreating a shop"""

    class Meta:
        model = Shop
        fields = "__all__"
