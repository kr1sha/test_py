from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    bio = models.TextField(default="no bio", verbose_name='Описание пользователя')
    avatar = models.ImageField(upload_to='avatars', default='no_picture.png', verbose_name='Аватар пользователя')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f"Profile of user: {self.user.username}"



