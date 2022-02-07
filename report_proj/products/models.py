from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name='Имя')
    image = models.ImageField(upload_to='products', default='no_picture.png', verbose_name='Фото')
    price = models.FloatField(help_text="in US dollars $", verbose_name='Цена')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f"{self.name}-{self.created.strftime('%d/%m/%Y')}"

