from rest_framework import serializers

from .models import Shop


class ShopListSerializer(serializers.ModelSerializer):
    """List shops"""

    city = serializers.SlugRelatedField(slug_field='title', read_only=True)
    street = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Shop
        fields = ['id', 'title', 'city', 'street', 'house', 'time_open', 'time_close', 'created_at', 'update_at']


class ShopCreateSerializer(serializers.ModelSerializer):
    """Сreating a shop"""

    class Meta:
        model = Shop
        fields = ['id', 'title', 'city', 'street', 'house', 'time_open', 'time_close']
