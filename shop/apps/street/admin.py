from django.contrib import admin

from . import models


@admin.register(models.Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'city',  'created_at', 'update_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', )

