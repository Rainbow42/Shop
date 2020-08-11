from django.db import models


class Shop(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    # city = ManyToManyField(City, verbose_name='Город')
    street = models.CharField(max_length=255, verbose_name='Улица')
    house = models.CharField(max_length=255, verbose_name='Дом')
    time_open = models.TimeField(verbose_name='Время открытия')
    time_close = models.TimeField(verbose_name='Время закрытия')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Обновленно')

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
        ordering = ['created_at']

    def __str__(self) -> str:
        return self.title
