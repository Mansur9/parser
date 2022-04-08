from unicodedata import name
from django.db import models

class Network(models.Model):
    url = models.CharField(max_length=512, verbose_name='Ссылка')
    name = models.CharField(max_length=512, verbose_name='Название')
    description  = models.CharField(max_length=512, blank=True, default="", verbose_name='Анонс')

    class Meta:
        verbose_name_plural = "Торговые сети"
        verbose_name = "Торговая сеть"
    

    def __str__(self):
        # return f"{self._meta.model_name} object {self.id}"
        # return f"ха-ха {self.name} {self.url}"
        return self.name

    
    def __str__(self):
        return self.name

class About(models.Model):
    verbose_description = models.CharField(max_length=512, verbose_name=" About")

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"


    