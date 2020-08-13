from rest_framework import serializers
from .models import City


class CityListSerializer(serializers.ModelSerializer):
    """List of cities"""
    class Meta:
        model = City
        fields = ['id', 'title', 'created_at']
