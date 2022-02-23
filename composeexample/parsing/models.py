from unicodedata import name
from django.db import models

class Network(models.Model):
    url = models.CharField(max_length=512, verbose_name='Ссылка')
    name = models.CharField(max_length=512, verbose_name='Название')

    class Meta:
        verbose_name_plural = "Торговые сети"
        verbose_name = "Торговая сеть"
