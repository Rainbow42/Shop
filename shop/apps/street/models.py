from django.db import models

from apps.city.models import City


class Street(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, verbose_name='Город')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Обновленно')

    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'
        ordering = ['created_at']

    def __str__(self) -> str:
        return self.title
