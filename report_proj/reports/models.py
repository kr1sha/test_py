from django.db import models
from django.urls import reverse

from profiles.models import Profile


class Report(models.Model):
    name = models.CharField(max_length=120, verbose_name='Наименование')
    image = models.ImageField(upload_to='reports', blank=True, verbose_name='Изображение')
    remark = models.TextField(verbose_name='Примечания')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Автор заметки')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('reports:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ('-created',)

