from django.contrib import admin

from . import models


@admin.register(models.Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'street', 'house', 'time_open', 'time_close', 'created_at', 'update_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
