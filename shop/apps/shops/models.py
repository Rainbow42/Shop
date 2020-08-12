from django.db import models
from apps.city.models import City
from apps.street.models import Street
from django.http import HttpResponse


class Shop(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, verbose_name='Город')
    street = models.ForeignKey(Street, on_delete=models.SET_NULL, null=True, verbose_name='Улица')
    house = models.CharField(max_length=255, verbose_name='Дом')
    time_open = models.TimeField(verbose_name='Время открытия', help_text='время в формате  00:00')
    time_close = models.TimeField(verbose_name='Время закрытия', help_text='время в формате  00:00')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Обновленно')

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
        ordering = ['created_at']

    def __str__(self) -> str:
        return self.title

