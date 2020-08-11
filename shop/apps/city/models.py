from django.db import models


class City(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

