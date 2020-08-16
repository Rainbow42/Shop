from django_filters import rest_framework as filters
from django_filters import rest_framework as rest_filters, NumberFilter, CharFilter
from .models import Shop


class ShopFilter(filters.FilterSet):
    title = CharFilter(lookup_expr='icontains')
    city = CharFilter(field_name='city__title')
    street = CharFilter(field_name='street__title')

    class Meta:
        model = Shop
        fields = ['title', 'city', 'street']
