from rest_framework import serializers

from .models import Street


class StreetDetailCitySerializer(serializers.ModelSerializer):
    """List of all streets in the city"""

    city = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Street
        fields = ['id', 'city', 'title', 'created_at']
