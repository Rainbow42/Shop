from apps.street.models import Street
from django.contrib import admin, messages
from . import models
from .models import Shop


@admin.register(models.Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'city', 'street', 'house', 'time_open', 'time_close', 'created_at', 'update_at')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

    def save_model(self, request, obj, form, change):
        """Checking for the existence of streets in the city"""
        street = Street.objects.get(title=str(obj.street))
        if street.city == obj.city:
            super(ShopAdmin, self).save_model(request, obj, form, change)
        else:
            messages.set_level(request, messages.ERROR)
            messages.error(request, 'No changes are permitted ..')
