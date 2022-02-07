from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=128, verbose_name='Имя')
    logo = models.ImageField(upload_to='customers', default='no_picture.png', verbose_name='Лого')

    def __str__(self):
        return str(self.name)

