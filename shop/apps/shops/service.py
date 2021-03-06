from django_filters import CharFilter, NumberFilter
from django_filters import rest_framework as filters
from django_filters import rest_framework as rest_filters

from .models import Shop


class ShopFilter(filters.FilterSet):
    city = CharFilter(field_name='city__title')
    street = CharFilter(field_name='street__title')

    class Meta:
        model = Shop
        fields = ['city', 'street']
