# Generated by Django 4.0.1 on 2022-01-31 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Имя')),
                ('image', models.ImageField(default='no_picture.png', upload_to='products', verbose_name='Фото')),
                ('price', models.FloatField(help_text='in US dollars $', verbose_name='Цена')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateField(auto_now=True, verbose_name='Дата последнего изменения')),
            ],
        ),
    ]
